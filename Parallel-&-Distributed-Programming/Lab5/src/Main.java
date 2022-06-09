import domain.Polynomial;
/**
 * The multiplication of 2 polynomials.
 * Both the regular O(n^2) algorithm and the Karatsuba algorithm are used,
 * each in both the sequential form and the parallelized form.
 */

public class Main {
    public static void main(String[] args) {
        Polynomial p = new Polynomial(22);
        Polynomial q = new Polynomial(22);

        System.out.println("\nP:" + p);
        System.out.println("Q:" + q + "\n");

        // Regular O(n^2)
        runAndMeasureRegularSequential(p,q);
        runAndMeasureRegularThreaded(p,q);

        // Karatsuba
        runAndMeasureKaratsubaSequential(p,q);
        runAndMeasureKaratsubaThreaded(p,q);
    }

    private static void runAndMeasureRegularSequential(Polynomial p, Polynomial q) {
        long start = System.currentTimeMillis();
        Polynomial result = MultiplicationAlgorithms.regularSequential(p, q);
        long end = System.currentTimeMillis();
        System.out.println("Regular sequential polynomials multiplication: ");
        System.out.println("- execution time: " + (end - start) + " ms");
        System.out.println("- result: " + result + "\n");
    }

    private static void runAndMeasureRegularThreaded(Polynomial p, Polynomial q) {
        long start = System.currentTimeMillis();
        Polynomial result = MultiplicationAlgorithms.regularThreaded(p, q);
        long end = System.currentTimeMillis();
        System.out.println("Regular threaded polynomials multiplication: ");
        System.out.println("- execution time: " + (end - start) + " ms");
        System.out.println("- result: " + result + "\n");
    }

    private static void runAndMeasureKaratsubaSequential(Polynomial p, Polynomial q) {
        long start = System.currentTimeMillis();
        Polynomial result = MultiplicationAlgorithms.karatsubaSequential(p, q);
        long end = System.currentTimeMillis();
        System.out.println("Karatsuba sequential polynomials multiplication: ");
        System.out.println("- execution time: " + (end - start) + " ms");
        System.out.println("- result: " + result + "\n");
    }

    private static void runAndMeasureKaratsubaThreaded(Polynomial p, Polynomial q) {
        long start = System.currentTimeMillis();
        Polynomial result = MultiplicationAlgorithms.karatsubaThreaded(p, q, 0);
        long end = System.currentTimeMillis();
        System.out.println("Karatsuba threaded polynomials multiplication: ");
        System.out.println("- execution time: " + (end - start) + " ms");
        System.out.println("- result: " + result + "\n");
    }
}
