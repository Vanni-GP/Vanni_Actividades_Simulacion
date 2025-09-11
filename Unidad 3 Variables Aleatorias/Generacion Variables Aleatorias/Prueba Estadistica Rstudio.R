# Descripción: Prueba Chi-cuadrado con Shiny
library(shiny)

ui <- fluidPage(
  titlePanel("Prueba Estadística"),
  actionButton("probar", "Chi-cuadrado"),
  textOutput("resultado")
)

server <- function(input, output){
  observeEvent(input$probar, {
    observadas <- c(18,22,20)
    esperadas <- c(20,20,20)
    test <- chisq.test(x=observadas, p=esperadas/sum(esperadas))
    output$resultado <- renderText({ paste("Chi2 =", round(test$statistic,2), "p =", round(test$p.value,4)) })
  })
}

shinyApp(ui = ui, server = server)
