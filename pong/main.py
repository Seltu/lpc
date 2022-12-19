import turtle
# import os
import functools


# draw screen
screen = turtle.Screen()
screen.title("My Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)


def draw_paddle(position):
    paddle = turtle.Turtle()
    paddle.speed(0)
    paddle.shape("square")
    paddle.color("white")
    paddle.shapesize(stretch_wid=5, stretch_len=1)
    paddle.penup()
    paddle.goto(position, 0)

    return paddle


# draw paddle
paddles = [draw_paddle(-345), draw_paddle(345)]

# draw ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = 1

# score
score_1 = 0
score_2 = 0

# head-up display
hud = turtle.Turtle()
hud.speed(0)
hud.shape("square")
hud.color("white")
hud.penup()
hud.hideturtle()
hud.goto(0, 260)
hud.write("0 : 0", align="center", font=("Press Start 2P", 24, "normal"))


def paddle_up(paddle):
    y = paddles[paddle].ycor()
    if y < 250:
        y += 30
    else:
        y = 250
    paddles[paddle].sety(y)


def paddle_down(paddle):
    y = paddles[paddle].ycor()
    if y > -250:
        y += -30
    else:
        y = -250
    paddles[paddle].sety(y)


def wall_score(score):
    score += 1
    hud.clear()
    hud.write("{} : {}".format(score_1, score_2), align="center", font=("Press Start 2P", 24, "normal"))
    # os.system("afplay 258020_kodack_arcade-bleep-4sound.wav&")
    ball.goto(0, 0)
    ball.dx *= -1
    return score


def collision_with_paddle(paddle, bounce):
    x, y = paddles[paddle].xcor(), paddles[paddle].ycor()
    if x + 10 > ball.xcor() > x - 10 and y + 50 > ball.ycor() > y - 50:
        ball.setx(x + bounce)
        ball.dx *= -1
        # os.system("afplay bounce.wav&")


# keyboard
screen.listen()
screen.onkeypress(functools.partial(paddle_up, 0), "w")
screen.onkeypress(functools.partial(paddle_down, 0), "s")
screen.onkeypress(functools.partial(paddle_up, 1), "Up")
screen.onkeypress(functools.partial(paddle_down, 1), "Down")


def move_ball():
    global score_1, score_2
    screen.update()
    # ball movement
    ball.setx(ball.xcor() + ball.dx*3)
    ball.sety(ball.ycor() + ball.dy*3)

    # collision with the upper wall
    if ball.ycor() > 290:
        # os.system("afplay bounce.wav&")
        ball.sety(290)
        ball.dy *= -1

    # collision with lower wall
    if ball.ycor() < -290:
        # os.system("afplay bounce.wav&")
        ball.sety(-290)
        ball.dy *= -1

    # collision with left wall
    if ball.xcor() < -380:
        score_1 = wall_score(score_1)

    # collision with right wall
    if ball.xcor() > 380:
        score_2 = wall_score(score_2)

    # collision with the paddle 1
    collision_with_paddle(0, 10)

    # collision with the paddle 2
    collision_with_paddle(1, -10)

    screen.ontimer(move_ball, 2)


move_ball()
turtle.mainloop()
