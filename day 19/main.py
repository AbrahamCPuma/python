from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_right():
    tim.right(5)

def turn_left():
    tim.left(5)

def clearscreen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    

screen.listen()
screen.onkeypress(key="w",fun=move_forwards)
screen.onkeypress(key="s",fun=move_backwards)
screen.onkeypress(key="a",fun=turn_right)
screen.onkeypress(key="d",fun=turn_left)
screen.onkey(key="c",fun=clearscreen)
screen.exitonclick()