import turtle
import math

turtle.tracer(60, 1)

# Draw Border
border = turtle.Turtle()
border.ht()


def draw_circle():
    border.penup()
    border.goto(-18, -250)
    border.pendown()
    for c in range(45):
        border.fd(35.5)
        border.left(8)

    #turtle.update()

    return 35.5 / math.sin(math.radians(8))


# Create Ball
ball = turtle.Turtle()
ball.ht()
ball.penup()


def draw_ball():
    ball.clear()

    ball.pendown()
    ball.fillcolor("blue")
    ball.begin_fill()
    for c in range(15):
        ball.fd(5)
        ball.left(24)
    ball.end_fill()
    ball.penup()

    #turtle.update()


def solve_theta():
    global theta
    if ball.ycor() == 0 and ball.xcor() < 0:
        theta = 1
    elif ball.ycor() == 0 and ball.xcor() > 0:
        theta = -1
    elif ball.ycor() == 0 and ball.xcor() == 0:
        theta = math.atan(d_orgin)
    else:
        theta = math.atan(ball.xcor() / ball.ycor())

    return theta


ball_hspd = -7
ball_vspd = 2

d_orgin = math.sqrt((ball.xcor() ** 2) + (ball.ycor() ** 2))
theta = solve_theta()


def move_ball():
    global ball_hspd, ball_vspd
    if d_orgin >= 255:
        if 0 < theta < 180:
            ball_vspd *= -1
            # ball_vspd = -1 * math.abs(ball_vspd)
        elif 180 < theta < 360:
            ball_vspd *= -1
            # ball_vspd = math.abs(ball_vspd)
        ball_hspd *= -1

    return 0


# Main Loop
radius = draw_circle()

t = 0

while True:
    draw_ball()
    move_ball()
    ball.goto(ball.xcor() + ball_hspd, ball.ycor() + ball_vspd)

    t += 1
    ball_vspd -= t * .05
    d_orgin = math.sqrt((ball.xcor() ** 2) + (ball.ycor() ** 2))
    theta = math.atan(ball.xcor() / ball.ycor())

    if t > 255:
        break
