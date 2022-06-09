import domain.Polynomial;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.*;
// https://en.wikipedia.org/wiki/Karatsuba_algorithm

public class MultiplicationAlgorithms {
    static int NO_OF_THREADS = 4;

    public static Polynomial regularSequential(Polynomial p1, Polynomial p2) {
        int resCoefLen = p1.getDegree() + p2.getDegree() + 1;
        List<Integer> resCoefficients = new ArrayList<>();
        for (int i = 0; i < resCoefLen; i++) resCoefficients.add(0);

        for (int i = 0; i < p1.getCoefficients().size(); i++)
            for (int j = 0; j < p2.getCoefficients().size(); j++)
            {
                int product = p1.getCoefficients().get(i) * p2.getCoefficients().get(j);
                resCoefficients.set(i+j, resCoefficients.get(i+j) + product);
            }
        return new Polynomial(resCoefficients);
    }

    public static Polynomial regularThreaded(Polynomial p1, Polynomial p2)  {
        int resCoefLen = p1.getDegree() + p2.getDegree() + 1;
        List<Integer> resCoefficients = new ArrayList<>();
        for (int i = 0; i < resCoefLen; i++) resCoefficients.add(0);
        Polynomial result = new Polynomial(resCoefficients);

        ThreadPoolExecutor executor = (ThreadPoolExecutor) Executors.newFixedThreadPool(NO_OF_THREADS);
        int threadSliceLen = (resCoefLen + NO_OF_THREADS - 1) / NO_OF_THREADS;  // ceil

        for(int i=0; i<resCoefLen; i += threadSliceLen){
            int finalI = i;
            executor.submit(() -> {
                for (int index = finalI; index < finalI + threadSliceLen; index++) {
                    if (index > result.coefficients.size()) return;
                    for (int j = 0; j <= index; j++) {
                        if (j < p1.coefficients.size() && (index - j) < p2.coefficients.size()) {
                            int product = p1.getCoefficients().get(j) * p2.getCoefficients().get(index - j);
                            result.coefficients.set(index, result.coefficients.get(index) + product);
                        }
                    }
                }
            });
        }
        executor.shutdown();
        try {
            var r = executor.awaitTermination(22, TimeUnit.SECONDS);
            if (!r) System.out.println("Regular threads did not finish.");
        }
        catch (InterruptedException ignored){}
        return result;
    }

    public static Polynomial karatsubaSequential(Polynomial p1, Polynomial p2) {
        if (p1.getDegree() < 2 || p2.getDegree() < 2)   // recursion stop condition
            return regularSequential(p1, p2);

        int len = Math.max(p1.getDegree(), p2.getDegree()) / 2;  // n/2
        Polynomial lowerP1 = new Polynomial(p1.getCoefficients().subList(0, len));
        Polynomial upperP1 = new Polynomial(p1.getCoefficients().subList(len, p1.coefficients.size()));
        Polynomial lowerP2 = new Polynomial(p2.getCoefficients().subList(0, len));
        Polynomial upperP2 = new Polynomial(p2.getCoefficients().subList(len, p2.coefficients.size()));

        Polynomial z0 = karatsubaSequential(lowerP1, lowerP2);
        Polynomial z1 = karatsubaSequential(Polynomial.add(lowerP1, upperP1), Polynomial.add(lowerP2, upperP2));
        Polynomial z2 = karatsubaSequential(upperP1, upperP2);

        // compute the result
        // (z2 × 10^n) + ((z1 - z2 - z0) × 10^len) + z0
        Polynomial r1 = Polynomial.addPrefixZeroCoefficients(z2, 2 * len);
        Polynomial r2 = Polynomial.addPrefixZeroCoefficients(Polynomial.subtract(Polynomial.subtract(z1, z2), z0), len);
        return Polynomial.add(Polynomial.add(r1, r2), z0);
    }

    public static Polynomial karatsubaThreaded(Polynomial p1, Polynomial p2, int depth) {
        if (p1.getDegree() < 2 || p2.getDegree() < 2)   // recursion stop condition
            return regularSequential(p1, p2);

        if (depth >= NO_OF_THREADS)     // depth control
            return karatsubaSequential(p1, p2);

        int len = Math.max(p1.getDegree(), p2.getDegree()) / 2;  // n/2
        Polynomial lowerP1 = new Polynomial(p1.getCoefficients().subList(0, len));
        Polynomial upperP1 = new Polynomial(p1.getCoefficients().subList(len, p1.coefficients.size()));
        Polynomial lowerP2 = new Polynomial(p2.getCoefficients().subList(0, len));
        Polynomial upperP2 = new Polynomial(p2.getCoefficients().subList(len, p2.coefficients.size()));

        ExecutorService executor = Executors.newFixedThreadPool(NO_OF_THREADS);
        Future<Polynomial> f0 = executor.submit(() -> karatsubaThreaded(lowerP1, lowerP2, depth + 1));
        Future<Polynomial> f1 = executor.submit(() -> karatsubaThreaded(Polynomial.add(lowerP1, upperP1), Polynomial.add(lowerP2, upperP2), depth + 1));
        Future<Polynomial> f2 = executor.submit(() -> karatsubaThreaded(upperP1, upperP2, depth + 1));

        executor.shutdown();
        Polynomial result = null;
        try {
            Polynomial z0 = f0.get();
            Polynomial z1 = f1.get();
            Polynomial z2 = f2.get();
            var r = executor.awaitTermination(22, TimeUnit.SECONDS);
            if (!r) System.out.println("Karatsuba threads did not finish.");

            // compute the result
            // (z2 × 10^n) + ((z1 - z2 - z0) × 10^len) + z0
            Polynomial r1 = Polynomial.addPrefixZeroCoefficients(z2, 2 * len);
            Polynomial r2 = Polynomial.addPrefixZeroCoefficients(Polynomial.subtract(Polynomial.subtract(z1, z2), z0), len);
            result = Polynomial.add(Polynomial.add(r1, r2), z0);
        }
        catch (InterruptedException | ExecutionException ignored){}

        return result;
    }

}
