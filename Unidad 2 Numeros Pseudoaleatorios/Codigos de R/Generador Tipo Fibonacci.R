fibonacci_rng <- function(n, seed1=7, seed2=11, m=1000) {
  valores <- numeric(n)
  x <- seed1
  y <- seed2
  for (i in 1:n) {
    z <- (x + y) %% m
    valores[i] <- z / m
    x <- y
    y <- z
  }
  return(valores)
}

valores <- fibonacci_rng(10)
cat("Números pseudoaleatorios generados en R:\n")
print(valores)

