from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake")
screen.bgcolor("black")

x_coord = 0
for _ in range(3):
    segment = Turtle(shape="square")
    segment.color("white")
    segment.goto(x=x_coord, y=0)
    x_coord -= 20

screen.exitonclick()
