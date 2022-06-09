// a bonus
// https://en.wikipedia.org/wiki/Karatsuba_algorithm
import java.util.Random;
import java.math.BigInteger;

public class BigNumbersMultiplication {
    public static void main(String[] args) {
        int noOfDigits = 22;
        BigInteger a = generate(noOfDigits);
        BigInteger b = generate(noOfDigits);
        System.out.println("Big a: " + a);
        System.out.println("Big b: " + b);
        BigInteger res = multiplyKaratsubaBigNr(a, b);
        System.out.println("Result: "  + res);
    }

    private static BigInteger generate(int digits) {
        StringBuilder number = new StringBuilder();
        Random r = new Random();
        for (int i = 0; i < digits; i++) number.append(r.nextInt(10));
        return new BigInteger(number.toString());
    }

    private static BigInteger multiplyKaratsubaBigNr(BigInteger x, BigInteger y) {
        int len = Math.min(x.toString().length(), y.toString().length());
        if (len < 10)
            return x.multiply(y);
        len /= 2;

        String xs = x.toString();
        String ys = y.toString();

        BigInteger high1 = new BigInteger(xs.substring(0, xs.length() - len));
        BigInteger low1 = new BigInteger(xs.substring(xs.length() - len));
        BigInteger high2 = new BigInteger(ys.substring(0, ys.length() - len));
        BigInteger low2 = new BigInteger(ys.substring(ys.length() - len));

        BigInteger z1 = multiplyKaratsubaBigNr(low1, low2);
        BigInteger z2 = multiplyKaratsubaBigNr(low1.add(high1), low2.add(high2));
        BigInteger z3 = multiplyKaratsubaBigNr(high1, high2);

        BigInteger r1 = addZeros(z3, 2 * len);
        BigInteger r2 = addZeros(z2.subtract(z3).subtract(z1), len);
        return r1.add(r2).add(z1);
    }

    private static BigInteger addZeros(BigInteger num, int offset) {
        return new BigInteger(num.toString() + "0".repeat(Math.max(0, offset)));
    }

}
