import java.util.Random;

public class NumerosPseudoAleatorios {
    public static void main(String[] args) {
        Random generador = new Random(43); // Semilla fija para reproducibilidad
        int totalPuntos = 10000;
        int puntosDentro = 0;

        for (int i = 0; i < totalPuntos; i++) {
            double x = generador.nextDouble();
            double y = generador.nextDouble();

            if (x * x + y * y < 1) {
                puntosDentro++;
            }
        }

        double piEstimado = (double) puntosDentro / totalPuntos * 4;
        System.out.println("Estimación de pi usando Monte Carlo: " + piEstimado);
    }
}
