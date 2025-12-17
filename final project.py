from color_palate import RandomColor
from turtle import Turtle, Screen
import random
screen = Screen()
screen.colormode(255)
timy = Turtle()
timy.speed("fastest")
timy.hideturtle()
timy.penup()

timy.setheading(225)
timy.forward(300)
timy.setheading(0)

color = RandomColor.colorgram_color()

dot_count = 100
for count in range(1,dot_count + 1):
    timy.dot(20, random.choice(color))
    timy.forward(50)

    if count % 10 == 0:
        timy.setheading(90)
        timy.forward(50)
        timy.setheading(180)
        timy.forward(500)
        timy.setheading(0)


screen.exitonclick()