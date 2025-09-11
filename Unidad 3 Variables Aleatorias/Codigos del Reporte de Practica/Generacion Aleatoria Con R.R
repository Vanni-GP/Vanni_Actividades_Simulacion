library(tcltk)

# Generar números aleatorios
entero <- sample(0:99, 1)
decimal <- runif(1, 0.0, 1.0)

# Mostrar en ventana emergente
mensaje <- paste("Número entero aleatorio:", entero, "\nNúmero decimal aleatorio:", decimal)
tkmessageBox(title = "Resultados", message = mensaje)

