package domain;

import java.util.Random;

public final class Matrix {
    public final int n,m;
    public int [][] matrix;

    public Matrix(int n, int m) {
        this.n = n;  // no. of rows
        this.m = m;  // no. of columns
        this.matrix = new int [n][m];
    }

    public void populate() {
        Random random = new Random();
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                matrix[i][j] = random.nextInt(99) + 1;
    }

    public int get(int row, int column) {
        return matrix[row][column];
    }

    public void set(int row, int column, int value) {
        matrix[row][column] = value;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++)
                sb.append(matrix[i][j]).append(" ");
            sb.append("\n");
        }
        return sb.toString();
    }
}