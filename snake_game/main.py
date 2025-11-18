from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
#Setup screen and game
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# start the game
game_is_on = True
while game_is_on:
    
    screen.update()     # with the tracer= 0, the screen tneeds to be updated to show the changes made in the following for loop.
    time.sleep(0.1)     # add 10 miliseconds delay like "fps" to refresh the screen
    snake.move()
        

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -280:
       scoreboard.reset()
       snake.reset()
        

    for segment in snake.segments[1:]:
        
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            











screen.exitonclick()