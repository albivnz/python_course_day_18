import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255) # module property can be 1.0 or 255

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

timmy = Turtle()
timmy.speed('fastest')

print("Random Color is: ", random_color())

angle = 5

for _ in range(int(360/angle)):
    timmy.color(random_color())
    timmy.circle(100)
    timmy.setheading(timmy.heading() + angle)

screen = Screen()
screen.exitonclick()
