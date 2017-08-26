import turtle

my_turtle = turtle.Turtle()

def circle(length, angle):

  my_turtle.forward(length)
  my_turtle.right(angle)
  my_turtle.forward(length)
  my_turtle.right(angle)
  my_turtle.forward(length)
  my_turtle.right(angle)
  my_turtle.forward(length)
  my_turtle.right(110)
  

for i in range(100):
  circle(50,90)
