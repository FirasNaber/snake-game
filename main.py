import time
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake")
screen.bgcolor("black")

screen.tracer(0)

x_coord = 0
segments = []
for _ in range(3):
    segment = Turtle(shape="square")
    segment.color("white")
    segment.penup()
    segment.goto(x=x_coord, y=0)
    segments.append(segment)
    x_coord -= 20

game_over = False
while not game_over:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(segments) - 1, 0, -1):
        segments[seg_num].goto(segments[seg_num - 1].pos())
    segments[0].forward(20)

screen.exitonclick()
