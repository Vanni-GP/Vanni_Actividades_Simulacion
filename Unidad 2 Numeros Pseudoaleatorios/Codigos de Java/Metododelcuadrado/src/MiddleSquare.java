public class MiddleSquare {
    public static double[] middleSquare(int seed, int n) {
        double[] valores = new double[n];
        int num = seed;

        for (int i = 0; i < n; i++) {
            num = num * num;
            String s = String.format("%08d", num);
            String middle = s.substring(2, 6);
            num = Integer.parseInt(middle);
            valores[i] = num / 10000.0;
        }
        return valores;
    }

    public static void main(String[] args) {
        double[] numeros = middleSquare(5735, 10);
        System.out.println("Números pseudoaleatorios generados en Java:");
        for (double v : numeros) {
            System.out.println(v);
        }
    }
}
