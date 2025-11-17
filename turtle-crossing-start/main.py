import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# -- SCREEN SETUP

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Cross the Road")
screen.tracer(0)

# -- FUNCTIONS

def moving():
    for cars in all_cars:
        cars.move_car()

def increase_moving():
    for cars in all_cars:
        cars.increase_speed()

#objects

turtle = Player()
scoreboard = Scoreboard()

#create FIRST car objects

all_cars = []
for car in range(20):
    all_cars.append(CarManager())

#controls

screen.listen()
screen.onkey(turtle.move_up,"Up")


#game loop

loop_count = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    moving()

# -- CAR GENERATOR 
   
    loop_count += 1
    if loop_count % 4 == 0:     # -- create cars every second
        match scoreboard.level:
            case 1:
                all_cars.append(CarManager(STARTING_X_MIN= 310,STARTING_X_MAX=400))
            case 2:
                all_cars.append(CarManager(STARTING_X_MIN= 310,STARTING_X_MAX=400, Increment= 10)) 
            case 3:
                all_cars.append(CarManager(STARTING_X_MIN= 310,STARTING_X_MAX=400, Increment= 20)) 
            case 4:
                all_cars.append(CarManager(STARTING_X_MIN= 310,STARTING_X_MAX=400, Increment= 30))  
            case _:
                all_cars.append(CarManager(STARTING_X_MIN= 310,STARTING_X_MAX=400, Increment= 30))  

# -- CAR DESTROYER
    for car in all_cars:
        if car.xcor() <-350:
            all_cars.remove(car)
            car.hideturtle()
    
# -- CAR COLLITION
    for car in all_cars:
        distance_x = abs(turtle.xcor() - car.xcor())
        distance_y = abs(turtle.ycor() - car.ycor())
        if distance_x < 25 and distance_y < 18:
            game_is_on = False
            scoreboard.gameover()

# -- LEVEL UP

    if turtle.ycor() > 300:
        turtle.reset_turtle()
        scoreboard.increase_level()
        increase_moving()
        
    



screen.exitonclick()