def generador_congruencial(seed, n):
    a = 1103515245
    c = 12345
    m = 2**31
    numeros = []
    x = seed
    for _ in range(n):
        x = (a * x + c) % m
        numeros.append(x / m)
    return numeros

valores = generador_congruencial(seed=42, n=10)
print("Números pseudoaleatorios generados en Python:")
print(valores)

