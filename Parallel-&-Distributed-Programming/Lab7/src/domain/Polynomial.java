package domain;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Polynomial implements Serializable {
    public int degree;
    public List<Integer> coefficients;

    public Polynomial(int degree) {
        this.degree = degree;
        this.coefficients = new ArrayList<>(degree + 1);
        Random r = new Random();
        for (int i = 0; i < degree; i++)
            coefficients.add(r.nextInt(22));
        coefficients.add(r.nextInt(22) + 1);  // preserve the degree
    }

    public Polynomial(List<Integer> coefficients) {
        this.degree = coefficients.size() - 1;
        this.coefficients = coefficients;
    }

    public int getDegree() {
        return degree;
    }

    public List<Integer> getCoefficients() {
        return coefficients;
    }

    public static Polynomial add(Polynomial p1, Polynomial p2) {
        int minDegree = Math.min(p1.getDegree(), p2.getDegree());
        int maxDegree = Math.max(p1.getDegree(), p2.getDegree());
        List<Integer> coefficients = new ArrayList<>(maxDegree + 1);
        for (int i = 0; i <= minDegree; i++)
            coefficients.add(
                    p1.getCoefficients().get(i) + p2.getCoefficients().get(i) );

        addRemainingCoefficients(p1, p2, minDegree, maxDegree, coefficients);
        return new Polynomial(coefficients);
    }

    public static Polynomial subtract(Polynomial p1, Polynomial p2) {
        int minDegree = Math.min(p1.getDegree(), p2.getDegree());
        int maxDegree = Math.max(p1.getDegree(), p2.getDegree());
        List<Integer> coefficients = new ArrayList<>(maxDegree + 1);
        for (int i = 0; i <= minDegree; i++)
            coefficients.add(
                    p1.getCoefficients().get(i) - p2.getCoefficients().get(i) );

        addRemainingCoefficients(p1, p2, minDegree, maxDegree, coefficients);
        int i = coefficients.size() - 1;              // degree may have reduced
        while (coefficients.get(i) == 0 && i > 0) {
            coefficients.remove(i);
            i--;
        }

        return new Polynomial(coefficients);
    }

    private static void addRemainingCoefficients(Polynomial p1, Polynomial p2, int minDegree, int maxDegree, List<Integer> coefficients) {
        if (maxDegree == p1.getDegree()) {
            for (int i = minDegree + 1; i <= maxDegree; i++)
                coefficients.add(p1.getCoefficients().get(i));
        } else {
            for (int i = minDegree + 1; i <= maxDegree; i++)
                coefficients.add(p2.getCoefficients().get(i));
        }
    }

    public static Polynomial addPrefixZeroCoefficients(Polynomial p, int offset) {
        List<Integer> coefficients = new ArrayList<>(offset);
        for(int i=0; i<offset; i++) coefficients.add(0);
        coefficients.addAll(p.getCoefficients());
        return new Polynomial(coefficients);
    }

    @Override
    public String toString(){
        StringBuilder str = new StringBuilder();
        for (int i = 0; i <= degree; i++) {
            if (coefficients.get(i) == 0) continue;
            str.append(" ").append(coefficients.get(i)).append("x^").append(i).append(" +");
        }
        str.deleteCharAt(str.length() - 1);
        return str.toString();
    }

    public static Polynomial getZeroedPolynomial(int degree){
        List<Integer> zeros = IntStream.range(0, degree).mapToObj(i -> 0).collect(Collectors.toList());
        return new Polynomial(zeros);
    }

}
