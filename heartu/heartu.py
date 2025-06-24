import turtle

def curve(step_forward: int, step_steer: int, distance: int, is_right: bool):
  for i in range(distance):
    if is_right:
      turtle.right(step_steer)
    else:
      turtle.left(step_steer)
    turtle.forward(step_forward)

def heart():
  turtle.color('red', 'red')
  turtle.begin_fill()

  turtle.left(140)
  turtle.forward(111.65)

  curve(2, 2, 100, True)

  turtle.left(120)

  curve(2, 2, 100, True)

  turtle.forward(111.65)

  turtle.end_fill()

if __name__ == '__main__':
  turtle.speed(2)
  turtle.bgcolor('black')
  turtle.pensize(3)

  # heartu
  heart()

  # I
  turtle.penup()
  turtle.pensize(15)
  turtle.color('white')
  turtle.goto(-200, 170)
  turtle.pendown()
  turtle.goto(-160, 170)
  turtle.penup()
  turtle.goto(-180, 170)
  turtle.left(50)
  turtle.pendown()
  turtle.forward(170)
  turtle.penup()
  turtle.goto(-200, 0)
  turtle.pendown()
  turtle.goto(-160, 0)

  # U
  turtle.penup()
  turtle.goto(160, 170)
  turtle.pendown()
  turtle.forward(110)
  curve(2, 2, 90, False)
  turtle.forward(108)

  turtle.done()
