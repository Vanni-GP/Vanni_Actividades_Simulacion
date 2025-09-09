import random

def estimar_pi(cantidad_puntos, semilla=45):
    random.seed(semilla)
    dentro_del_circulo = 0

    for _ in range(cantidad_puntos):
        x = random.random()
        y = random.random()
        if x**2 + y**2 < 1:
            dentro_del_circulo += 1

    return (dentro_del_circulo / cantidad_puntos) * 4

# Ejecución
total = 10000
pi_estimado = estimar_pi(total)
print(f"Estimación de π con {total} puntos: {pi_estimado:.5f}")
