
// Descripción: Aproxima una N(0,1) sumando 12 variables uniformes
import java.util.Random;

public class Convolucion {
    public static void main(String[] args) {
        Random rand = new Random();
        double suma = 0;
        for (int i = 0; i < 12; i++) {
            suma += rand.nextDouble();
        }
        double normal = suma - 6;
        System.out.println("Variable por convolución: " + normal);
    }
}
