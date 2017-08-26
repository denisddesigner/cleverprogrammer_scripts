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

square(100, 45)
square(150, 50)
square(100, 60)
