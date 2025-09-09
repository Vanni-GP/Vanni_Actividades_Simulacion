set.seed(123)

n <- 30
datos <- runif(n)

media <- mean(datos)

signos <- ifelse(datos >= media, 1, -1)

corridas <- 1
for (i in 2:length(signos)) {
  if (signos[i] != signos[i-1]) {
    corridas <- corridas + 1
  }
}

cat("Datos:", datos, "\n")
cat("Número de corridas:", corridas, "\n")

