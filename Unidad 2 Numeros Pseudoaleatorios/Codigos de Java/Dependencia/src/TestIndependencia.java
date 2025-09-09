import java.util.Random;

public class TestIndependencia {
    public static void main(String[] args) {
        int n = 100;
        double[] datos = new double[n];
        Random rnd = new Random();

        for (int i = 0; i < n; i++) {
            datos[i] = rnd.nextDouble();
        }

        double mediaX = 0, mediaY = 0;
        for (int i = 0; i < n-1; i++) {
            mediaX += datos[i];
            mediaY += datos[i+1];
        }
        mediaX /= (n-1);
        mediaY /= (n-1);

        double num = 0, denX = 0, denY = 0;
        for (int i = 0; i < n-1; i++) {
            num += (datos[i] - mediaX) * (datos[i+1] - mediaY);
            denX += Math.pow(datos[i] - mediaX, 2);
            denY += Math.pow(datos[i+1] - mediaY, 2);
        }
        double correlacion = num / Math.sqrt(denX * denY);

        System.out.println("Coeficiente de correlación: " + correlacion);
    }
}
