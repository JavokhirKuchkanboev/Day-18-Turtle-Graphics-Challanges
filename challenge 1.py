import random
from turtle import Turtle, Screen
import random
from color_palate import RandomColor

timy = Turtle()

screen =Screen()
screen.colormode(255)
angles = 3


while angles != 8:
    timy.color(RandomColor.random_color())
    for n in range(angles):
        timy.forward(100)
        timy.right(360/angles)

    angles += 1





screen.exitonclick()
