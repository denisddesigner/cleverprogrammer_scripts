import turtle

my_turtle=turtle.Turtle() 

# Sqaure

def square(length, angle):

    
    
    my_turtle.forward(length)
    my_turtle.right(angle)
    my_turtle.forward(length)
    my_turtle.right(angle)
    my_turtle.forward(length)
    my_turtle.right(angle)
    my_turtle.forward(length)


for i in range(20):
    square(50, 90)

