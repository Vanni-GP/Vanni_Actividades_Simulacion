
// Descripción: Combina dos distribuciones usando probabilidad 30%-70%
import java.util.Random;

public class Composicion {
    public static void main(String[] args) {
        Random rand = new Random();
        double u = rand.nextDouble();
        double x = (u < 0.3) ? rand.nextDouble() * 2 : 2 + rand.nextDouble() * 3;
        System.out.println("Variable por composición: " + x);
    }
}
