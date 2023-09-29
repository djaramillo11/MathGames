
#$$$

rect_base = 4
rect_height = 4
#rect_base = round(random(1,7))
#rect_height = round(random(1,5))

#$$$

def setup():
  global ans, squareButton,input, information
  createCanvas(500,500)
  #area, width, height
  #squareButton = createButton("")
  #squareButton.size(50,50)
  #squareButton.position(125,100)

  input = createInput()
  input.position(410, 95)
  input.size(40,30)
  input.value("0")
  input.style('background-color', 'transparent') 
  input.style('border', 'transparent') 

  information=""


  
def draw():
  global ans, squareButton,information
  background("#a89c")
  # drawTickAxes()
  stroke("white")
  fill("#538790")
  textSize(30)
  textAlign(CENTER,CENTER)

  drawRectangle()

  # strokeWeight(2)
  push()
  # noStroke()
  textFont("cursive")
  strokeWeight(2)

  text(f"Base = {rect_base},",75,75)
  text(f"Height = {rect_height},",220,75)
  #text(f"Area = {rect_base * rect_height}",370,75)
  text("Area=",360,75)
  textSize(25)
  text("Demonstration:", 250, 480)
  text("Input the area of the rectangle:", 230, 450)
  pop()
  textSize(20)
  text("Area = b x h", 250, 120)
  
  fill("yellow")
  text(information,250,30)

  getResponse()

def getResponse():
  global information
  value = 0 if input.value() == '' else int(input.value())
  if value is not rect_height*rect_base:
    information="Incorrect"
  else:
    information="correct"
    
  
#the user's rectangle
def drawRectangle():
  push()
  strokeWeight(2)
  stroke("white")
  # fill(0,255,0,100)
  fill("#355C7D")
  rectMode(CENTER)
  rect(250,300,rect_base*50,rect_height*50)
  drawHorArrow(250 - rect_base*25,280 - rect_height*25,250+ rect_base*25,280 - rect_height*25)
  text(rect_base, 250,260 - rect_height*25)
  drawVertArrow(230 -rect_base*25,300 - rect_height*25, 230 -rect_base*25,300 + rect_height*25)
  text(rect_height, 215 -rect_base*25,300)

  pop()

def drawVertArrow(x1,y1,x2,y2):

  push()
  strokeWeight(2.5)
  #x1, y1, x2, y2
  #points are from bottom to top
  line(x1,y1,x2,y2)
  pop()
  #first arrow
  line(x1, y1, x1 -10, y1 + 10)
  line(x1, y1, x1 +10, y1 + 10)
  #other arrow
  line(x2, y2, x2 -10, y2 - 10)
  line(x2, y2, x2 +10, y2 - 10)

def drawHorArrow(x1,y1,x2,y2):
  
  push()
  strokeWeight(2.5)
  #points are from left to right
  line(x1,y1,x2,y2)
  pop()
  #first arrow
  line(x1, y1, x1 +10, y1 - 10)
  line(x1, y1, x1 +10, y1 + 10)
  #other arrow
  line(x2, y2, x2 -10, y2 - 10)
  line(x2, y2, x2 -10, y2 + 10)




