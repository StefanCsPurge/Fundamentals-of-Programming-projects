import core.MatrixMultiplicationTask;
import domain.Matrix;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

/** Threaded matrix multiplication
 *
 * Splitting the work between tasks:
 * -> each task computes every k-th element (k is the no. of the task) from the result matrix, going row by row
*/

public class Main {
    private static final int numOfCores = Runtime.getRuntime().availableProcessors();
    private static final int NO_OF_THREADS = 12;
    private static final String APPROACH = "ThreadPool";   ///  NormalThreads/ThreadPool

    private static final int rows1 = 5;
    private static final int cols1 = 5;
    private static final int rows2 = 5;
    private static final int cols2 = 5;

    public static void main(String[] args) {
        System.out.println("This system has " + numOfCores + " cores.\n");
	    Matrix a = new Matrix(rows1, cols1);
	    Matrix b = new Matrix(rows2, cols2);
        if(a.m != b.n){
            System.err.println("Matrix multiplication not possible: cols1 != rows2");
            return;
        }

        a.populate();
        b.populate();
        System.out.println(a);
        System.out.println(b);

        Matrix result = new Matrix(a.n, b.m);

        double start_time = System.currentTimeMillis();

        if(APPROACH.equals("NormalThreads")){
            runNormalThreads(a,b,result);
        }
        else if (APPROACH.equals("ThreadPool")){
            runThreadPool(a,b,result);
        }
        else
            System.err.println("Invalid value for the APPROACH parameter/");

        double end_time = System.currentTimeMillis();
        double execution_time_s = end_time / 1000.0 - start_time / 1000.0;
        double execution_time_ms = end_time - start_time;

        System.out.println("The result is:\n" + result);
        System.out.println("No. of threads: " + NO_OF_THREADS + " | approach: " + APPROACH);
        System.out.println("Execution time: " + execution_time_s + " s  /  " + execution_time_ms + " ms\n");
        System.out.println(NO_OF_THREADS + " | " + APPROACH + " | " + rows1 + "x" + cols1 + " | " + rows2 + "x" + cols2 + " | " + execution_time_s + " s  (" + execution_time_ms + " ms)");
    }

    public static void runNormalThreads(Matrix a, Matrix b, Matrix result){
        List<Thread> threads = new ArrayList<>();
        for(int i = 0; i < NO_OF_THREADS; i++)
            threads.add(new MatrixMultiplicationTask(i,a,b,result,NO_OF_THREADS));

        for(Thread thread : threads)
            thread.start();

        // the threads are now computing the multiplication

        for(Thread thread: threads)
            try {  // terminate the threads by joining them with the main thread
                thread.join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
    }

    public static void runThreadPool(Matrix a, Matrix b, Matrix result){
        ExecutorService service = Executors.newFixedThreadPool(NO_OF_THREADS);

        for(int i = 0; i < NO_OF_THREADS; i++)
            service.submit(new MatrixMultiplicationTask(i,a,b,result,NO_OF_THREADS));

        service.shutdown();
        try {
            if (!service.awaitTermination(420, TimeUnit.SECONDS))
                service.shutdownNow();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
