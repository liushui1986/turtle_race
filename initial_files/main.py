from turtle import Turtle, Screen
import random

race_on = False
turtle_pass_number = 0  # if one turtle pass the finish line, the number will be added 1.
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter the color: ')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtles = []

# Define 6 turtles and assign them in the start line
for i in range(6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=-100 + 40 * i)
    turtles.append(new_turtle)

# If the user gives the bet, the race will start
if user_bet:
    race_on = True

# When race starts, all turtles will run together and give the final orders passing the finish line.
while race_on:
    for turtle_ in turtles:
        distance = random.randint(0, 10)  # Turtle will run length of random number between 0 and 10
        turtle_.forward(distance)

        if turtle_.xcor() > 230:  # When the turtle pass the finish line, the color will be recorded as winning_turtle
            winning_turtle = turtle_.pencolor()

            # Here it ensures only the #1 runner will be used for bet and tell you the results
            if turtle_pass_number == 0:
                if user_bet == winning_turtle:
                    print(f'Your bet is {user_bet}.')
                    print(f"You've won! The {winning_turtle} turtle is the winner!\n")
                else:
                    print(f'Your bet is {user_bet}.')
                    print(f"You've lost! The {winning_turtle} turtle is the winner!\n")

            # The other conditions will give you the order of the runners finishing the race.
            else:
                winning_turtle = turtle_.pencolor()
                print(f'The {winning_turtle} turtle is the No.{turtle_pass_number + 1}!')

            # After each record, the recorded turtle will be removed and the turtle_pass_number will be added 1.
            turtles.remove(turtle_)
            turtle_pass_number += 1

            if turtle_pass_number == 6:
                race_on = False
                break

screen.exitonclick()
