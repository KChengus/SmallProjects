import turtle as td
import random

num = 50
val = [-num, num]
colors = ["black", "yellow", "brown", "green", "blue", "pink", "gray", "red"]
def random_walking():
    return val[random.randint(0, 1)]

def direction():
    return random.randint(0, 360)

def check_pos():
    x,y = td.pos()
    if not (-350 <= x <= 350 and -300 <= y <= 300):
        td.penup()
        td.goto(0, 0)
        td.pencolor(random.choice(colors))
        td.pendown()


td.hideturtle()
td.pensize(10)
td.speed(10)
while True:
    try:

        td.forward(random_walking())
        td.left(direction())
        check_pos()
    except td.Terminator:
        break