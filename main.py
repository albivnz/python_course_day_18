import turtle as t
import random
import math

timmy = t.Turtle()
side_length = 100
print(f"Default speed is {timmy.speed()}")
speed = 0
timmy.speed(speed)
print(f"Speed set to {speed}")

for sides in range(3,11):
    angle = 360/sides
    red = random.random()
    blue = random.random()
    green = random.random()
    timmy.pencolor(red, blue, green)
    print(f"RGB color for {sides} sides polygon is: {red:.2f}, {blue:.2f}, {green:.2f}")
    for n in range(sides):
        timmy.forward(side_length)
        timmy.left(angle)

input("Press enter to continue")
timmy.clear()

timmy.pensize(3)
dash_length = 10
number_of_iterations = 500
timmy.screen.colormode(255) 

for i in range(number_of_iterations):
    angle = 90*(math.ceil(random.random()*4))
    red = random.randint(0,255)
    blue = random.randint(0,255)
    green = random.randint(0,255)
    timmy.pencolor(red, blue, green)
    print(f"Random angle in iteration {i} is: {angle})")
    timmy.right(angle)
    timmy.forward(dash_length)

input("Press enter to continue")
