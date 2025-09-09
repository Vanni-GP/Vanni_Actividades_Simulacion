set.seed(101)

simular_dados <- function(n=100000) {
  exitos <- 0
  for (i in 1:n) {
    dado1 <- sample(1:6, 1, replace=TRUE)
    dado2 <- sample(1:6, 1, replace=TRUE)
    if (dado1 == 6 || dado2 == 6) {
      exitos <- exitos + 1
    }
  }
  return(exitos / n)
}

probabilidad <- simular_dados()
cat("Probabilidad de obtener al menos un 6 en dos dados:", probabilidad, "\n")
