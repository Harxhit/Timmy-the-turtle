# pip install colorgram.py  ### In your terminal 

# import colorgram

# rgb_colors = []   ### This is the code to how to extract color from any image

# colors = colorgram.extract("image.jpg" , 30)

# for color in colors :
#   r = color.rgb.r
#   g = color.rgb.g
#   b = color.rgb.b
#   new_color = (r,g,b)
#   rgb_colors.append(new_color)
  
# print(rgb_colors)
 
from turtle import Turtle ,Screen

import random

timmy = Turtle()
timmy.shape("turtle")
screen = Screen()
screen.colormode(255)


color_list = [(230, 228, 224), (236, 241, 238), (241, 236, 240), (198, 159, 116), (70, 92, 129), (147, 85, 53), (218, 210, 116), (138, 160, 191), (178, 160, 38), (184, 146, 164), (28, 32, 46), (58, 34, 23), (120, 70, 93), (139, 175, 154), (77, 115, 79), (143, 25, 16), (186, 97, 82), (61, 31, 42), (121, 27, 41), (45, 58, 94), (177, 96, 114), (102, 119, 170), (34, 52, 45), (100, 160, 85), (214, 175, 192), (216, 181, 173), (160, 209, 191), (67, 86, 23), (219, 206, 8)]

timmy.speed("fastest")

timmy.penup()

timmy.hideturtle()       ###### You can hide your turtle from here
timmy.setheading(225)
timmy.forward(250)
timmy.setheading(0)

number_of_dots = 101 

for dot_count in range(1, number_of_dots) :
  timmy.dot(20 , random.choice(color_list))
  timmy.forward(50)

  if dot_count % 10 == 0 : 
    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(180)
    timmy.forward(500)
    timmy.setheading(0)


screen.exitonclick()