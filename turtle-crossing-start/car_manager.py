from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager(Turtle):
    def __init__(self, shape = "square",STARTING_X_MIN = -260, STARTING_X_MAX = 500, Increment = 0):
        super().__init__(shape)
        self.y_rand = random.randint(-230,300)
        self.x_rand = random.randint(STARTING_X_MIN,STARTING_X_MAX)
        self.shapesize(stretch_len=2,stretch_wid=1)
        self.penup()
        self.color(random.choice(COLORS))
        self.goto(x=self.x_rand, y=self.y_rand)
        self.distance_speed = STARTING_MOVE_DISTANCE + Increment
        
    
    def move_car(self):
        
        x_pos = self.xcor() - self.distance_speed
        self.goto(x=x_pos,y=self.y_rand)

    def increase_speed(self):
        self.distance_speed += MOVE_INCREMENT

