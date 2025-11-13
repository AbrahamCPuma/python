import turtle 
import random

direction = ["right","left"]


def square(times):
    for i in range(times):
        tim.forward(100)
        tim.right(90)
        
def dot_line(lenght):
    for i in range(200):
        tim.forward(lenght)
        tim.penup()
        tim.forward(lenght)
        tim.pendown() 

def draw_shapes():
    for i in range(3,11):
       tim.pencolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
       shapes = i
       for i in range(shapes):
           tim.forward(100)
           tim.right(360/shapes)   

def random_walk():
    
    for i in range(100):
        rand_dir = random.choice(direction)
        rand_angle = random.randint(0,90)
        tim.pencolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        tim.forward(20)
        tim.setheading(rand_angle)

def rgb_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb = (r, g, b)
    return rgb

def spirograph(size):
    for i in range(int(360/size)):
       turtle_circle.setheading(turtle_circle.heading() + size)
       turtle_circle.color(rgb_color())
       turtle_circle.circle(100)

tim = turtle.Turtle()
turtle.colormode(255)
tim.shape("turtle")
tim.color("red4")
tim.pensize(5)
tim.speed(9)
tim.hideturtle()

turtle_circle = turtle.Turtle()
turtle.colormode(255)
turtle_circle.speed("fastest")




spirograph(20)

screen = turtle.Screen()
screen.exitonclick()