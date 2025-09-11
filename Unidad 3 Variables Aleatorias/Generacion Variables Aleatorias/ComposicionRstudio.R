# Descripción: Combina dos distribuciones
library(shiny)

ui <- fluidPage(
  titlePanel("Composición"),
  actionButton("generar", "Generar"),
  textOutput("resultado")
)

server <- function(input, output){
  observeEvent(input$generar, {
    u <- runif(1)
    x <- if(u<0.3) runif(1,0,2) else runif(1,2,5)
    output$resultado <- renderText({ paste("Variable por composición:", round(x,4)) })
  })
}

shinyApp(ui = ui, server = server)
