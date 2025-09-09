import random

def generar_numeros_aleatorios(cantidad, semilla=123):
    random.seed(semilla)
    lista_numeros = []

    for _ in range(cantidad):
        numero = random.random() * (20 - 5) + 5  # Escala a [5, 20]
        lista_numeros.append(numero)

    return lista_numeros

# Ejecución
total = 10
numeros = generar_numeros_aleatorios(total)
print(f"Lista de {total} números pseudoaleatorios entre 5 y 20:")
for i, num in enumerate(numeros, start=1):
    print(f"{i:02d}: {num:.5f}")
