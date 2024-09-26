import turtle as tl
import math as mt

#Draw Border
border = tl.Turtle()
border.ht()
tl.tracer(0)

def draw_circle():
  border.penup()
  border.goto(-18,-250)
  border.pendown()
  for c in range(45):
    border.fd(35.5)
    border.left(8)
  
  tl.update()
  
  return (35.5 / mt.sin(mt.radians(8)))

#Create Ball
ball = tl.Turtle()
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
  
  tl.update()

def solve_theta():
  return mt.degrees(mt.atan(ball.xcor() / ball.ycor()))


#Main Loop
radius = draw_circle()

hspd = 8
vspd = .00001

while True:
  draw_ball()
  ball.goto(ball.xcor() + hspd, ball.ycor() + vspd)
  if mt.sqrt(ball.xcor() ** 2 + ball.ycor() ** 2) > 255:
    theta = solve_theta()
    if 0 < theta < 90 and hspd > 0:
      hspd = -1 * abs(hspd)
      vspd = -1 * abs(vspd)
    elif 0 < theta < 90 and hspd < 0:
      hspd = abs(hspd)
      vspd = abs(vspd)
    elif -90 < theta < 0 and hspd > 0:
      hspd = -1 * abs(hspd)
      vspd = abs(vspd)
    elif -90 < theta < 0 and hspd < 0:
      hspd = abs(hspd)
      vspd = -1 * abs(vspd)
  if mt.sqrt(ball.xcor() ** 2 + ball.ycor() ** 2) > 305:
    break
