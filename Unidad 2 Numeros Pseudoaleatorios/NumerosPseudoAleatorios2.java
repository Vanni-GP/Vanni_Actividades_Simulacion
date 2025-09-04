import java.util.Random;

public class NumerosPseudoAleatorios2 {
    public static void main(String[] args) {
        Random generador = new Random(456); // Semilla fija para reproducibilidad
        int cantidad = 20;

        System.out.println("Generando " + cantidad + " números pseudoaleatorios entre 0 y 1:");

        for (int i = 0; i < cantidad; i++) {
            double numero = generador.nextDouble();
            System.out.printf("Número %2d: %.6f%n", i + 1, numero);
        }
    }
}
