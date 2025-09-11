import java.util.Random;

public class GeneracionAleatoria {
    public static void main(String[] args) {
        Random random = new Random();

        // Generar un número entero aleatorio entre 0 y 99
        int entero = random.nextInt(100);
        System.out.println("Número entero aleatorio: " + entero);

        // Generar un número decimal aleatorio entre 0.0 y 1.0
        double decimal = random.nextDouble();
        System.out.println("Número decimal aleatorio: " + decimal);
    }
}
