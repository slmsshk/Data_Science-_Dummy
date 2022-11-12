library(shiny)
ui <- fluidPage(
  titlePanel("Prediction"),
  sidebarLayout(
    sidebarPanel(
      numericInput("num","Hp",1),
      numericInput("num1","VOL",1),
      numericInput("num2","SP",1),
      numericInput("num3","Weight",1)
    ),
    mainPanel(
      tableOutput("distplot")
      
    )
  )
)
server <- function(input, output) {
  output$distplot <- renderTable({
    
    Cars <- read.csv("C:/Users/Slmss/Desktop/excelr/Deployment/Cars.csv")
    
    model.car <- lm(MPG~.,data=Cars)
    nw=data.frame(HP=input$num,VOL=input$num1,SP=input$num2,WT=input$num3)
    nw
    w=predict(model.car,nw)
    w
  })
  
  
  
  xyz<-datasets::quakes
  
}

shinyApp(ui = ui, server = server)