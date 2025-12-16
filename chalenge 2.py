from color_palate import RandomColor
from turtle import Turtle, Screen
import random
screen = Screen()
screen.colormode(255)


timy = Turtle()
timy.pensize(15)
timy.speed("fastest")
direction = [0, 90, 180, 270] #right or left

for _ in range(200):
    timy.color(RandomColor.random_color())
    timy.forward(30)
    timy.setheading(random.choice(direction))

screen.exitonclick()