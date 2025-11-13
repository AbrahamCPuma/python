from turtle import Screen, Turtle
from snake import Snake
import time
#Setup screen and game
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

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
        


















screen.exitonclick()