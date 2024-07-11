from turtle import Turtle , Screen
import random 


screen = Screen()
screen.setup(width = 500 , height = 300)
user_bets = screen.textinput(title= "Place your bet :" , prompt= "Which turtle will win the race ? Choose the colour :")
colors = ["orange","blue" , "yellow" , "green" , "red" ]
y_positions = [-70, -40, -10, 20, 50, 80]
list_turtle = []

race_on = False 

for turtle_index in range(len(colors)) : 

  new_turtle = Turtle()
  new_turtle.shape("turtle")
  new_turtle.color(colors[turtle_index])
  new_turtle.penup()
  new_turtle.goto(x = -230 , y = y_positions[turtle_index] )
  list_turtle.append(new_turtle)
  

if user_bets :
  race_on = True

while race_on :
  for turtle in list_turtle :
    if turtle.xcor() > 230 : 
      race_on = False 
      winning_color = turtle.pencolor()
      if winning_color == user_bets :
        print(f"You won! The {winning_color} is winning turtle..")
      else :
        print(f"You lost! The {winning_color} is winning turtle..")
        break
    random_distance = random.randint(0,10)
    turtle.forward(random_distance)
      


  























screen.exitonclick()