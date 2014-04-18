# server.R

library(shiny)


shinyServer(function(input, output) {


  output$distPlot <- renderPlot({

    # generate an rnorm distribution and plot it
    dist <- rnorm(input$obs)
    hist(dist)
  })
})
