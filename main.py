import random
import turtle as t


# Initiate screen objects
screen = t.Screen()
screen_width = 500
screen_height = 400
screen.setup(width=screen_width, height=screen_height)

# Dynamically create all six turtles
turtles = []
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_size = screen_height / 175
starting_line = screen_width / -2 + (turtle_size * 10)
finish_line = screen_width / 2 - (turtle_size * 20)

for n in range(6):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[n])
    new_turtle.turtlesize(stretch_wid=turtle_size, stretch_len=turtle_size)
    new_turtle.setposition(x=starting_line, y=screen_height / 7 * (n + 1) - (screen_height / 2))
    turtles.append(new_turtle)

# Ask the user to choose who they think will win
user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle will win the race? Enter a color: ")

# The race
winner = False
while not winner:
    for turtle in turtles:
        if turtle.xcor() > finish_line:
            winner = True
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle is the winner!")
            else:
                print(f"You lost. The {winning_color} turtle is the winner.")

        distance = random.randint(0, 10)
        turtle.forward(distance)

screen.exitonclick()
