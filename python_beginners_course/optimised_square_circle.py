import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(0)
my_turtle.color("green")


def circle(length, angle):
   for i in range(4):
      my_turtle.forward(length)
      my_turtle.right(angle)


for i in range(360):
    circle(100, 90)
    my_turtle.left(13)
    circle(100, 90)
    


