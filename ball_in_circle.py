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
  #ball.clear()
  
  ball.pendown()
  ball.fillcolor(abs(hspd) * .92, abs(vspd) * 4.6, abs(t) * 19)
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

hspd = 260
vspd = 30

t = 0
while True:
  draw_ball()
  ball.goto(ball.xcor() + hspd/2, ball.ycor() + vspd/2 + t)
  
  #Checks which quadrant edge the ball hits and adjusts velocities
  if mt.sqrt(ball.xcor() ** 2 + ball.ycor() ** 2) > radius:
    theta = solve_theta()
    
    #Represents drag, friction, heat loss, ect.
    hspd *= .99
    vspd *= .99
    
    if 0 < theta < 90 and hspd > 0:			#Quadrant 1
      hspd = -1 * abs(hspd)
      vspd = -1 * abs(vspd)
    elif 0 < theta < 90 and hspd < 0:		#Quadrant 4
      hspd = abs(hspd)
      vspd = abs(vspd)
      t = 0
    elif -90 < theta < 0 and hspd > 0:	#Quadrant 3
      hspd = -1 * abs(hspd)
      vspd = abs(vspd)
      t = 0
    elif -90 < theta < 0 and hspd < 0:	#Quadrant 2
      hspd = abs(hspd)
      vspd = -1 * abs(vspd)
    
    #Moves the ball to the edge of the circle
    temp_x = radius * (ball.xcor() / mt.sqrt(ball.xcor() ** 2 + ball.ycor() ** 2))
    temp_y = radius * (ball.ycor() / mt.sqrt(ball.xcor() ** 2 + ball.ycor() ** 2))
    ball.goto(temp_x, temp_y)
    
  t -= .981
  
  #Once ball comes to a rest, end loop.
  if -0.1 < hspd < 0.1 and -0.1 < vspd < 0.1:
    ball.clear()
    tl.update()
    break
