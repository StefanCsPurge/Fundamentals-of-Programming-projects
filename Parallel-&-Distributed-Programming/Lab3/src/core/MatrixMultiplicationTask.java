package core;

import domain.Matrix;

public class MatrixMultiplicationTask extends Thread {

    final int start_i, start_j, result_size, k, no_of_threads;
    int  task_no_elems;
    public Matrix a, b, result;

    public MatrixMultiplicationTask(int k, Matrix a, Matrix b, Matrix result, int no_of_threads){
        this.k = k;
        this.no_of_threads = no_of_threads;
        this.a = a;
        this.b = b;
        this.result = result;
        this.result_size = result.n * result.m;
        this.start_i = k / result.m;  // look for how many columns there are, to see on which row it should be
        this.start_j = k % result.m;
        this.task_no_elems = this.result_size/no_of_threads + ((k < this.result_size%no_of_threads) ? 1:0);
    }

    public static int computeElement(Matrix a, Matrix b, int elRow, int elCol) throws Exception {
        if (elRow >= a.n || elCol >= b.m)
            throw new Exception("Result element index out of bounds!");
        int element = 0;
        for (int k = 0; k < a.m; k++)
            element += a.get(elRow,k) * b.get(k,elCol);
        return element;
    }

    @Override
    public void run() {
        int i = start_i, j = start_j;
        while(this.task_no_elems > 0){
            try {
                result.set(i, j, computeElement(a,b,i,j));
            } catch (Exception e) {
                e.printStackTrace();
            }
            i += (j + this.no_of_threads) / result.m;
            j = (j + this.no_of_threads) % result.m;
            this.task_no_elems--;
        }
    }

}
