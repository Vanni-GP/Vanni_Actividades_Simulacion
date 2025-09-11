# Descripción: Genera un número decimal aleatorio y lo muestra en la app
library(shiny)

ui <- fluidPage(
  titlePanel("Variable Aleatoria Continua"),
  actionButton("generar", "Generar Número"),
  textOutput("resultado")
)

server <- function(input, output){
  observeEvent(input$generar, {
    numero <- runif(1, 0, 1)
    output$resultado <- renderText({ paste("Número continuo:", round(numero, 4)) })
  })
}

shinyApp(ui = ui, server = server)
