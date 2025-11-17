from turtle import Turtle

#player constants

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):       #-- Init player class
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.color("black")
        self.goto(STARTING_POSITION)

    def move_up(self):           #-- Move method
        self.forward(MOVE_DISTANCE)     

    def reset_turtle(self):
        self.goto(STARTING_POSITION)
    
