set.seed(231)

n <- 10000

x <- runif(n)
y <- runif(n)

# Usamos la ecuación del círculo: x² + y² < 1
dentro_del_circulo <- x^2 + y^2 < 1

pi_estimado <- sum(dentro_del_circulo) / n * 4

print(pi_estimado)


