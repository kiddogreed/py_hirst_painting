from random import choice
import turtle
from turtle import Turtle, Screen
turtle1 = Turtle()
turtle.colormode(255)

color_list = [(224, 234, 229), (176, 48, 79), (42, 98, 146), (205, 161, 94), (223, 210, 102), (137, 90, 64),
              (177, 164, 38), (109, 176, 207), (212, 131, 173), (227, 73, 49), (201, 75, 117), (88, 105, 192),
              (28, 143, 89)]

def jager():
    bturtle = Turtle()
    bturtle.pensize(20)
    bturtle.shape("circle")
    bturtle.penup()
    startline = bturtle.setpos(-335, -260)
    for _ in range(60):
        if _ % 4 == 0:
            bturtle.pendown()
            bturtle.forward(20)
        else:
            bturtle.penup()
            bturtle.forward(20)
turtle1.speed("fast")
turtle1.penup()
turtle1.hideturtle()
turtle1.setheading(225)
turtle1.forward(300)
turtle1.setheading(0)

number_of_dots = 100

for dot_count in range(1,number_of_dots+1):
    turtle1.dot(20, choice(color_list))
    turtle1.forward(50)

    if dot_count % 10 == 0 :
        turtle1.setheading(90)
        turtle1.forward(50)
        turtle1.setheading(180)
        turtle1.forward(500)
        turtle1.setheading(0)

screen = Screen()
screen.exitonclick()