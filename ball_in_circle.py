import turtle
import math

#Draw Border
border = turtle.Turtle()
border.ht()
border.tracer(0)

def draw_circle():
  border.penup()
  border.goto(-18,-250)
  border.pendown()
  for c in range(45):
    border.fd(35.5)
    border.left(8)
  
  border.update()
  
  return (35.5 / math.sin(math.radians(8)))

#Create Ball
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
  
  ball.update()

ball_hspd = 8
ball_vspd = 0

def move_ball():
  global ball_hspd
  if(-radius >= ball.xcor() or ball.xcor() >= radius):
    ball_hspd = -ball_hspd
  return 0

#Main Loop
radius = draw_circle()

t = 0

while(True):
  draw_ball()
  move_ball()
  ball.goto(ball.xcor() + ball_hspd, ball.ycor() + ball_vspd)
  
  t += 1
  if(t > 255):
    break
