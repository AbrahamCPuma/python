from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()
print(user_bet)
colors = ["red","green","orange","yellow","blue","purple"]
all_turtles = []

y = -125
x = -230
colorindex = 0

for turtle in range(6):
    
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[colorindex])
    new_turtle.shapesize(stretch_wid=1,stretch_len=1)
    new_turtle.penup()
    new_turtle.goto(x= x , y= y)
    all_turtles.append(new_turtle)
    y += 50
    colorindex += 1

print(all_turtles)
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230 :
            is_race_on = False
            turtle.shapesize(stretch_wid=1.5,stretch_len=1.5)
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
              print(f"You've won! The {winning_color} turtle is the winner")
            else:
              print(f"You've lost! The {winning_color} turtle is the winner")
             

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
screen.exitonclick()