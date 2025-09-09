import random

def chi_square_test(n=1000, k=10):
    datos = [random.random() for _ in range(n)]

    frecuencias = [0] * k
    for d in datos:
        index = int(d * k)
        if index == k:
            index = k-1
        frecuencias[index] += 1

    esperado = n / k
    chi = sum((f - esperado)**2 / esperado for f in frecuencias)

    print("Frecuencias observadas:", frecuencias)
    print("Valor Chi-cuadrada:", chi)

chi_square_test()
