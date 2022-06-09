import domain.Polynomial;

import java.util.ArrayList;
import java.util.List;
// https://en.wikipedia.org/wiki/Karatsuba_algorithm

public class MultiplicationAlgorithms {

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

    public static Polynomial regularSequentialSlice(Object o1, Object o2, int begin, int end) {
        Polynomial p = (Polynomial) o1;
        Polynomial q = (Polynomial) o2;
        Polynomial result = Polynomial.getZeroedPolynomial(p.getDegree()*2 + 1);
        for (int i = begin; i < end; i++) {
            for (int j = 0; j < q.getCoefficients().size(); j++)
                result.getCoefficients()
                        .set(i+j, result.getCoefficients().get(i+j) + p.getCoefficients().get(i) * q.getCoefficients().get(j));
        }
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



    public static Polynomial buildFinalResult(Object[] results) {
        int degree = ((Polynomial) results[0]).getDegree();
        Polynomial result = Polynomial.getZeroedPolynomial(degree+1);
        for (int i = 0; i < result.getCoefficients().size(); i++) {
            for (Object o : results)
                result.getCoefficients()
                        .set(i, result.getCoefficients().get(i) + ((Polynomial) o).getCoefficients().get(i));
        }
        return result;
    }

}
