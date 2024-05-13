import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Dice Rolling Simulator")

# Draw the dice
dice = turtle.Turtle()
dice.color("white")
dice.hideturtle()
dice.penup()
dice.speed(0)

def draw_square(t, size):
    t.penup()
    t.goto(-size / 2, size / 2)
    t.pendown()
    for _ in range(4):
        t.forward(size)
        t.right(90)

def draw_dot(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.dot(20)

def draw_dice_face(number):
    dice.clear()
    draw_square(dice, 200)

    if number == 1:
        draw_dot(dice, 0, 0)
    elif number == 2:
        draw_dot(dice, -50, 50)
        draw_dot(dice, 50, -50)
    elif number == 3:
        draw_dot(dice, -50, 50)
        draw_dot(dice, 0, 0)
        draw_dot(dice, 50, -50)
    elif number == 4:
        draw_dot(dice, -50, 50)
        draw_dot(dice, 50, 50)
        draw_dot(dice, -50, -50)
        draw_dot(dice, 50, -50)
    elif number == 5:
        draw_dot(dice, -50, 50)
        draw_dot(dice, 50, 50)
        draw_dot(dice, 0, 0)
        draw_dot(dice, -50, -50)
        draw_dot(dice, 50, -50)
    elif number == 6:
        draw_dot(dice, -50, 50)
        draw_dot(dice, 0, 50)
        draw_dot(dice, 50, 50)
        draw_dot(dice, -50, -50)
        draw_dot(dice, 0, -50)
        draw_dot(dice, 50, -50)

def roll_dice():
    number = random.randint(1, 6)
    draw_dice_face(number)
    screen.update()
    print(f"Rolled a {number}!")

# Set up rolling dice action
screen.listen()
screen.onkey(roll_dice, "space")

# Draw the initial dice face
draw_dice_face(1)
screen.update()

print("Press the spacebar to roll the dice.")
screen.mainloop()
