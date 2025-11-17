from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super(). __init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(1,1)
        self.penup()
        self.goto(0,0)
        self.x_move = 0.5
        self.y_move = 0.5
        self.move_speed = 0.005
    
    def reset_ball(self):
        self.goto(0,0)
        self.bounce_x()
        self.move_speed = 0.005
        
        

    def move(self):
        new_x_pos = self.xcor() + self.x_move
        new_y_pos = self.ycor() + self.y_move
        self.goto(new_x_pos,new_y_pos) 
    
    def bounce_y(self):
        self.y_move *= - 1

    def bounce_x(self):
        self.x_move *= - 1
        self.move_speed *=0.9