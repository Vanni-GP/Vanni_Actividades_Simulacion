import java.util.Random;

public class VariablesDiscretas {
    public static void main(String[] args) {
        Random rand = new Random();
        int dado = rand.nextInt(6) + 1;
        System.out.println("Numero aleatorio discreto (dado): " + dado);
    }
}
