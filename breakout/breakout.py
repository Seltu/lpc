import functools
import turtle
# import os
import math

# draw screen
screen = turtle.Screen()
screen.title("My Breakout")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# draw paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("blue")
paddle.shapesize(stretch_wid=0.5, stretch_len=2.5)
paddle.penup()
paddle.goto(0, -260)
paddle_direction = 0

# draw ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.shapesize(stretch_wid=0.5, stretch_len=0.5)
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = 1
last_pos = (0, 0)


def draw_block(pos):
    x, y = pos[0], pos[1]
    colors = ['yellow', 'green', 'orange', 'red']
    block = turtle.Turtle()
    block.color(colors[math.floor(y/2)])
    block.shape("square")
    block.shapesize(stretch_wid=0.5, stretch_len=2.5)
    block.penup()
    block.goto(x*55-360, 100+y*15)
    return block


# draw blocks
blocks = [[draw_block((i, j)) for i in range(14)] for j in range(8)]

# lives and score
lives = 4
score = 0

# head-up display
hud = turtle.Turtle()
hud.speed(0)
hud.shape("square")
hud.color("white")
hud.penup()
hud.hideturtle()
hud.goto(0, 260)
hud.write("Lives : 4 | Score : 0", align="center", font=("Press Start 2P", 18, "normal"))


def paddle_direct(direction):
    global paddle_direction
    paddle_direction = direction


def move_paddle():
    global paddle_direction
    x = paddle.xcor()
    if 380 > x + paddle_direction > -380:
        x += paddle_direction
    elif x + paddle_direction > -380:
        x = 380
    else:
        x = -380
    paddle.setx(x)


def collision(pos):
    x, y = pos[0], pos[1]
    global last_pos
    if x + 30 > ball.xcor() > x - 30 and y + 10 > ball.ycor() > y - 10:
        ball.dy *= -1
        ball.sety(ball.ycor()+ball.dy*10)
        # os.system("afplay bounce.wav&")
        return True
    return False


# keyboard
screen.listen()
screen.onkeypress(functools.partial(paddle_direct, 5), "Right")
screen.onkeypress(functools.partial(paddle_direct, -5), "Left")
screen.onkeyrelease(functools.partial(paddle_direct, 0), "Right")
screen.onkeyrelease(functools.partial(paddle_direct, 0), "Left")

draw = False


def move_ball():
    global draw, lives, score, last_pos
    fell = False
    move_paddle()
    # ball movement
    ball.setx(ball.xcor() + ball.dx*3)
    ball.sety(ball.ycor() + ball.dy*3)

    # collision with the upper wall
    if ball.ycor() > 290:
        # os.system("afplay bounce.wav&")
        ball.sety(290)
        ball.dy *= -1
        last_pos = (ball.xcor(), ball.ycor())

    # collision with lower wall
    if ball.ycor() < -290:
        lives -= 1
        hud.clear()
        hud.write("Lives : {} | Score : {}".format(lives, score), align="center", font=("Press Start 2P", 18, "normal"))
        # os.system("afplay 258020_kodack_arcade-bleep-4sound.wav&")
        ball.goto(last_pos)
        fell = True

    # collision with left wall
    if ball.xcor() < -380:
        ball.setx(-380)
        ball.dx *= -1
        if ball.ycor() > 100:
            last_pos = (ball.xcor(), ball.ycor())

    # collision with right wall
    if ball.xcor() > 380:
        ball.setx(380)
        ball.dx *= -1
        if ball.ycor() > 100:
            last_pos = (ball.xcor(), ball.ycor())

    # collision with paddle
    collision((paddle.xcor(), paddle.ycor()))

    # collision with blocks
    for i in range(len(blocks)):
        for block in blocks[i]:
            if collision((block.xcor(), block.ycor())):
                blocks[i].remove(block)
                block.hideturtle()
                score += 1+math.floor(i/2)*2
                hud.clear()
                hud.write("Lives : {} | Score : {}".format(lives, score), align="center",
                          font=("Press Start 2P", 18, "normal"))
    draw = True
    if not fell:
        if score < 448:
            screen.ontimer(move_ball, 10)
        else:
            hud.clear()
            hud.write("WINNER | Score : {}".format(lives, score), align="center",
                      font=("Press Start 2P", 18, "normal"))
            ball.color('black')
            screen.update()
    elif lives > 0:
        screen.update()
        screen.ontimer(move_ball, 1000)
    else:
        hud.clear()
        hud.write("GAME OVER | Score : {}".format(lives, score), align="center",
                  font=("Press Start 2P", 18, "normal"))
        ball.color('black')
        screen.update()


move_ball()


def update():
    global draw
    if draw:
        screen.update()
    draw = False
    screen.ontimer(update, 1)
    pass


update()
turtle.mainloop()
