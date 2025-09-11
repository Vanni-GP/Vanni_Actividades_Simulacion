# Descripción: Variable aleatoria exponencial usando transformada inversa
library(shiny)

ui <- fluidPage(
  titlePanel("Transformada Inversa"),
  actionButton("generar", "Generar"),
  textOutput("resultado")
)

server <- function(input, output){
  observeEvent(input$generar, {
    u <- runif(1)
    x <- -log(1-u)
    output$resultado <- renderText({ paste("Transformada inversa:", round(x,4)) })
  })
}

shinyApp(ui = ui, server = server)
