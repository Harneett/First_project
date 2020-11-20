import turtle
value = int(input("Enter the number of sides of the object"))

while 1:
    for steps in range(value):
        turtle.forward(100)
        turtle.right(360/value)
        for moresteps in range(value):
            turtle.forward(50)
            turtle.right(360/value)
