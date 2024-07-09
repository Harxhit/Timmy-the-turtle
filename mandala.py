import turtle

# Function to draw a line segment
def draw_line(length, angle):
    turtle.forward(length)
    turtle.right(angle)

# Function to draw a complex shape
def draw_shape(size, sides):
    angle = 360 / sides
    for _ in range(sides):
        draw_line(size, angle)

# Function to draw the mandala-like pattern
def draw_mandala():
    turtle.speed(0)  # Set the turtle speed to the maximum
    turtle.bgcolor("black")  # Set background color
    turtle.color("white")  # Set drawing color
    
    # Draw the mandala pattern
    for _ in range(36):  # Adjust the number of sections for complexity
        draw_shape(100, 4)  # Adjust size and sides for shape complexity
        turtle.left(10)  # Adjust angle for rotation
    
    turtle.hideturtle()
    turtle.done()

# Call the function to draw the mandala
draw_mandala()
