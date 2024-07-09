from turtle import Turtle ,  Screen
import random 

timmy =  Turtle()
timmy.shape("turtle")

screen = Screen()
screen.colormode(255)


def random_color() :
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  color = (r,g,b)
  return color

timmy.speed("fastest")

def spirograph(gap) :
  for  _ in range (int(360/gap)) :
    timmy.color(random_color())
    timmy.circle(100)
    timmy.setheading(timmy.heading() + gap)

spirograph(5)

screen.exitonclick()