import java.util.Random;

public class MonteCarloRuleta {
    public static void main(String[] args) {
        int n = 100000;
        double gananciaTotal = 0;
        Random rnd = new Random();

        for (int i = 0; i < n; i++) {
            double prob = rnd.nextDouble();
            if (prob < 0.5) {
                gananciaTotal += 10; // 50% gana 10
            } else if (prob < 0.8) {
                gananciaTotal -= 5; // 30% pierde 5
            } else {
                gananciaTotal -= 20; // 20% pierde 20
            }
        }

        double promedio = gananciaTotal / n;
        System.out.println("Promedio de ganancias en la ruleta: " + promedio);
    }
}
