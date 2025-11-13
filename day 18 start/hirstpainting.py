color_list= [(199, 175, 118), (125, 36, 24), (187, 158, 50), (170, 105, 56), (5, 57, 83), (222, 223, 226), (200, 216, 205), (108, 67, 85), (39, 36, 35), (86, 142, 58), (20, 123, 176), (110, 161, 175), (75, 39, 47), (9, 67, 47), (64, 153, 137), (133, 41, 43), (184, 98, 80), (179, 201, 186), (210, 200, 113), (179, 175, 177), (151, 176, 164), (93, 142, 156), (28, 80, 59), (194, 190, 192), (17, 78, 98), (213, 184, 173), (145, 116, 121), (176, 197, 202)]

import turtle as t
import random
def rand_color():
    rgb = random.choice(color_list)
    return rgb


pointer = t.Turtle()
pointer.hideturtle()
t.colormode(255)
pointer.speed("fastest")
pointer.teleport(-1000,-400)


for i in range(50):
    pointer.teleport(-1000,-400+(i*20))
    
    for i in range(40):
        pointer.pendown
        pointer.dot(20,rand_color())
        pointer.penup()
        pointer.forward(20)
        
        print(pointer.pos())


screen = t.Screen()
screen.exitonclick()