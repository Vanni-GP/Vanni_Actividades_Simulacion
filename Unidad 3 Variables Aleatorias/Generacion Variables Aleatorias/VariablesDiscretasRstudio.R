# Descripción: Genera un número entero aleatorio entre 1 y 6 y lo muestra en la app
library(shiny)

ui <- fluidPage(
  titlePanel("Variable Aleatoria Discreta"),
  actionButton("lanzar", "Lanzar Dado"),
  textOutput("resultado")
)

server <- function(input, output){
  observeEvent(input$lanzar, {
    dado <- sample(1:6, 1)
    output$resultado <- renderText({ paste("Dado:", dado) })
  })
}

shinyApp(ui = ui, server = server)
