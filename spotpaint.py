import colorgram
import turtle
import random

turtle.colormode(255)
margin = 20
dotsize = 15
rows = 10
dots_per_row = 16
spacing = 45

def setup_turtle():
    turtle_instance = turtle.Turtle()
    screen = turtle.Screen()
    screen.setworldcoordinates(-margin, -margin, screen.window_width() -margin, screen.window_height() - margin)

    return (turtle_instance, screen)


colors = colorgram.extract('image.jpg', rows * dots_per_row)

if isinstance(colors[0].rgb, tuple):
    print("First element extracted is a tuple!")
else:
    print("Warning: first element is not a tuple")


print("Listing colors extracted:")
for color in colors:
    print(color.rgb)


main_turtle, turtle_screen = setup_turtle()
main_turtle.speed('fastest')
main_turtle.penup()

for row in range(rows):
    for row_item_number in range(dots_per_row):
        #print(f"Position for {row_item_number}: {main_turtle.pos()}")
        main_turtle.dot(dotsize, random.choice(colors).rgb)
        main_turtle.forward(spacing)

    y_axis = main_turtle.pos()[1]
    main_turtle.setposition(0.0, y_axis + spacing)

main_turtle.home()
turtle_screen.exitonclick()
