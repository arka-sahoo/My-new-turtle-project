import turtle

screen = turtle.screen
screen.bgcolor("black")

pen = turtle.Turtle()
pen.speed(0)

colors = ["red", "yellow", "blue", "green", "orange", "purple"]

for i in range(100):
    pen.color(colors[i % len(colors)])
    pen.forward(i * 2)
    pen.right(50)

turtle.done()