# Descripción: Aproxima N(0,1) con suma de 12 números uniformes
library(shiny)

ui <- fluidPage(
  titlePanel("Convolución"),
  actionButton("generar", "Generar"),
  textOutput("resultado")
)

server <- function(input, output){
  observeEvent(input$generar, {
    suma <- sum(runif(12))
    normal <- suma - 6
    output$resultado <- renderText({ paste("Variable por convolución:", round(normal,4)) })
  })
}

shinyApp(ui = ui, server = server)
