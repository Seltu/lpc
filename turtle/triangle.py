import turtle
import random

wn = turtle.Screen()
t = turtle.Turtle()


def triangle(x, y):
    colors = ["black", "red", "green", "blue", "cyan", "magenta"]
    t.pencolor(random.choice(colors))
    t.pencolor()
    t.penup()
    t.goto(x, y)
    t.pendown()
    factor = random.randint(1, 6)/2
    for i in range(3):
        t.fd(50*factor)
        t.lt(120)
        t.fd(50*factor)


turtle.onscreenclick(triangle, 1)
turtle.listen()
turtle.done()
