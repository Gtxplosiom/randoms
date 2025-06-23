import turtle
import time

def curve(step_forward: int, step_steer: int, distance: int):
  for i in range(distance):
    turtle.forward(step_forward)
    turtle.right(step_steer)

def draw_ends(step_forward: int, step_steer: int, distance: int, left_1: int, left_2: int):
  curve(step_forward, step_steer, distance)

  turtle.left(left_1)

  curve(step_forward, step_steer, distance)

  turtle.left(left_2)

if __name__ == '__main__':
  turtle.speed(1)
  turtle.bgcolor('black')
  turtle.setpos([150, -150])
  turtle.pensize(3)
  turtle.color('white')

  turtle.colormode(255)
  turtle.fillcolor((181, 101, 29))

  turtle.begin_fill()

  draw_ends(2, 1, 250, 140, 90)

  turtle.forward(300)

  turtle.end_fill()
  time.sleep(2)
  turtle.undo()

  original_pos = turtle.pos()

  turtle.penup()
  turtle.goto(-200, 0)

  turtle.write("Woops! wrong color", align="center", font=("Arial", 12, "bold"))
  turtle.fillcolor('white')

  turtle.goto(original_pos)
  turtle.pendown()

  turtle.begin_fill()

  turtle.left(90)

  draw_ends(4, 2, 125, 138, 93)

  turtle.forward(300)

  turtle.left(90)

  draw_ends(8, 4, 62, 132, 94)

  turtle.forward(300)
  
  turtle.end_fill()
  turtle.penup()

  turtle.hideturtle()
  turtle.goto(150, 250)
  turtle.color('black')
  turtle.write("It's a Bone! ;D", align="center", font=("Arial", 16, "bold"))

  turtle.done()
