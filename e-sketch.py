from turtle import Turtle , Screen 

timmy = Turtle()

screen = Screen()

def front() :
  timmy.forward(100)
  
def back() :
  timmy.right(180)
  timmy.forward(100)

def rotate_clockwise() :
  timmy.right(340)

def rotate_anticlockwise () :
  timmy.left(340)
  
def draw() :
  timmy.forward(20)

def turn_right() :
  timmy.right(10)

def turn_left () :
  timmy.left(10)

def clear() :
  timmy.clear()
  timmy.penup()
  timmy.home()
  

screen.listen()
screen.onkey(key = "w" , fun = front)
screen.onkey(key = "s" , fun = back)
screen.onkey(key = "d" , fun = turn_right)
screen.onkey(key = "a" , fun = turn_left)
screen.onkey(key = "c" , fun = rotate_clockwise)
screen.onkey(key = "a" , fun = rotate_anticlockwise)
screen.onkey(key = "space" , fun = draw)
screen.onkey(key = "c" , fun = clear)


screen.exitonclick()