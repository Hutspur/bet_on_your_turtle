from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "green", "blue", "yellow", "purple", "coral"]
user_bet = screen.textinput(title="Make your stack!", prompt=f"which color of turtle will win: {colors}").lower()
y_coordinates = [-75, -45, -15, 15, 45, 75]
turtles = []
for number in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[number])
    new_turtle.goto(x=-230, y=y_coordinates[number])
    turtles.append(new_turtle)

if user_bet:
    gaming = True
    while gaming:
        for turtle in turtles:
            if gaming:
                turtle.forward(random.randint(0, 12))
            if turtle.xcor() >= 230:
                gaming = False
                if user_bet == turtle.pencolor():
                    print(f"You win! The {turtle.pencolor()} turtle finished first")
                else:
                    print(f"You loss! The {turtle.pencolor()} turtle finished first")




#
#
# def move_forward():
#     return tim.forward(10)
#
#
# def move_backward():
#     return tim.backward(10)
#
#
# def turn_left():
#     return tim.left(10)
#
#
# def turn_right():
#     return tim.right(10)
#
#
# screen.listen()
#
#
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="a", fun=turn_left)
# screen.onkey(key="d", fun=turn_right)


screen.exitonclick()
