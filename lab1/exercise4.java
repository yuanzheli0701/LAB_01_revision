public class exercise4{

    public static double evaluate(double[] coefficients, double x) {
        int n = coefficients.length;
        if (n == 0) return 0;
        double result = coefficients[n - 1];

        for (int i = n - 2; i >= 0; i--) {
            result = (result * x) + coefficients[i];
        }
        return result;
    }

    public static void main(String[] args) {
        double[] coeffs = {3.0, -2.0, 0.0, 5.0};
        double x = 2.0;
        System.out.println("Result of P(" + x + ") = " + evaluate(coeffs, x));
    }
}
