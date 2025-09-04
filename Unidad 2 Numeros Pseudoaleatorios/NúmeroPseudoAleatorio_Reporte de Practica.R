# Generar números pseudoaleatorios entre 20 y 50
set.seed(1)
numeros <- runif(10, min = 20, max = 50)

# Mostrar como tabla
data.frame(Índice = 1:10, Valor = round(numeros, 2))

promedio <- mean(numeros)
print(promedio)
