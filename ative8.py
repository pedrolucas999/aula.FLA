import turtle

leo = turtle.Turtle()

for _ in range(3):
    for _ in range(6):
        for _ in range(8):
            leo.forward(20)
            leo.right(30)
        leo.right(60)
    leo.penup()
    leo.forward(150)
    leo.pendown()