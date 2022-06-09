import domain.Polynomial;
/*
  The multiplication of 2 polynomials - using MPI.
  Both the regular O(n^2) algorithm and the Karatsuba algorithm are used.
 */
// https://stackoverflow.com/questions/36356408/mpj-express-java-mpi-running-in-intellij-idea
import mpi.MPI;  // using MPJ Express

public class Main {
    public static void main(String[] args) {
        MPI.Init(args);
        int currentProcess = MPI.COMM_WORLD.Rank();
        int nrProcesses = MPI.COMM_WORLD.Size();

        if (currentProcess == 0){
            // master process
            System.out.println("Master process - generating polynomials:");
            Polynomial p = new Polynomial(500);
            Polynomial q = new Polynomial(500);

            System.out.println("\nP:" + p);
            System.out.println("Q:" + q + "\n");
            runAndMeasureMultiplication(p,q,nrProcesses);
        }
        else
        {   /// choose the multiplication algorithm here

            /// Regular O(n^2)
            //workerRegular(currentProcess);

            /// Karatsuba
            workerKaratsuba(currentProcess);
        }
        MPI.Finalize();
    }

    private static void runAndMeasureMultiplication(Polynomial p, Polynomial q, int nrProcesses) {
        long startTime = System.currentTimeMillis();
        ////////////////////////////////////////////

        int start, finish = 0, sliceLen = p.coefficients.size() / (nrProcesses - 1);
        for (int i = 1; i < nrProcesses; i++) {
            start = finish;
            finish += sliceLen;
            if (i == nrProcesses - 1) finish = p.coefficients.size();

            // send polynomials
            MPI.COMM_WORLD.Send(new Object[]{p}, 0, 1, MPI.OBJECT, i, 0);
            MPI.COMM_WORLD.Send(new Object[]{q}, 0, 1, MPI.OBJECT, i, 0);

            // send slice boundaries
            MPI.COMM_WORLD.Send(new int[]{start}, 0, 1, MPI.INT, i, 0);
            MPI.COMM_WORLD.Send(new int[]{finish}, 0, 1, MPI.INT, i, 0);

        }

        Object[] partialResults = new Object[nrProcesses - 1];
        for (int i = 1; i < nrProcesses; i++)
            MPI.COMM_WORLD.Recv(partialResults, i - 1, 1, MPI.OBJECT, i, 0);

        Polynomial result = MultiplicationAlgorithms.buildFinalResult(partialResults);

        ////////////////////////////////////////////
        long endTime = System.currentTimeMillis();
        System.out.println("\nPolynomials multiplication done: ");
        System.out.println("- execution time: " + (endTime - startTime) + " ms");
        System.out.println("- result: " + result + "\n");
    }

    private static void workerRegular(int me) {
        System.out.printf("\n(workerRegular %d started)\n", me);

        Object[] p = new Object[2];
        Object[] q = new Object[2];
        int[] begin = new int[1];
        int[] end = new int[1];

        MPI.COMM_WORLD.Recv(p, 0, 1, MPI.OBJECT, 0, 0);
        MPI.COMM_WORLD.Recv(q, 0, 1, MPI.OBJECT, 0, 0);

        MPI.COMM_WORLD.Recv(begin, 0, 1, MPI.INT, 0, 0);
        MPI.COMM_WORLD.Recv(end, 0, 1, MPI.INT, 0, 0);

        Polynomial partialResult = MultiplicationAlgorithms.regularSequentialSlice(p[0], q[0], begin[0], end[0]);

        MPI.COMM_WORLD.Send(new Object[]{partialResult}, 0, 1, MPI.OBJECT, 0, 0);
    }

    private static void workerKaratsuba(int me) {
        System.out.printf("\n(workerKaratsuba %d started)\n", me);

        Object[] p = new Object[2];
        Object[] q = new Object[2];
        int[] begin = new int[1];
        int[] end = new int[1];

        MPI.COMM_WORLD.Recv(p, 0, 1, MPI.OBJECT, 0, 0);
        MPI.COMM_WORLD.Recv(q, 0, 1, MPI.OBJECT, 0, 0);

        MPI.COMM_WORLD.Recv(begin, 0, 1, MPI.INT, 0, 0);
        MPI.COMM_WORLD.Recv(end, 0, 1, MPI.INT, 0, 0);

        Polynomial _p = (Polynomial) p[0];
        Polynomial _q = (Polynomial) q[0];

        // keep only the slice we are interested in
        for (int i = 0; i < begin[0]; i++)
            _p.getCoefficients().set(i, 0);
        for (int j = end[0]; j < _p.getCoefficients().size(); j++)
            _p.getCoefficients().set(j, 0);

        Polynomial partialResult = MultiplicationAlgorithms.karatsubaSequential(_p, _q);

        MPI.COMM_WORLD.Send(new Object[]{partialResult}, 0, 1, MPI.OBJECT, 0, 0);
    }
}
