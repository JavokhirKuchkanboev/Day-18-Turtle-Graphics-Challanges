from color_palate import RandomColor
from turtle import Turtle, Screen
import random
screen = Screen()
screen.colormode(255)
timy = Turtle()
timy.speed("fastest")
current_heading = timy.heading()

for _ in range(100):
    timy.color(RandomColor.random_color())
    timy.circle(100)
    current_heading += 5
    timy.setheading(current_heading)


screen.exitonclick()