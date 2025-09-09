import random
import math

def montecarlo_sin(n=100000):
    dentro = 0
    for _ in range(n):
        x = random.uniform(0, math.pi)
        y = random.uniform(0, 1)
        if y <= math.sin(x):
            dentro += 1
    area = (dentro / n) * math.pi
    return area

resultado = montecarlo_sin()
print("Área aproximada bajo sin(x) en [0, π]:", resultado)
