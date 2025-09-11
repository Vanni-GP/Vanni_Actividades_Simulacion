
// Descripción: Genera una variable aleatoria exponencial usando transformada inversa
import java.util.Random;

public class TransformadaInversa {
    public static void main(String[] args) {
        Random rand = new Random();
        double u = rand.nextDouble();
        double x = -Math.log(1 - u);
        System.out.println("Transformada inversa: " + x);
    }
}
