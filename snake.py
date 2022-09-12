from turtle import Turtle

SEGMENT_SIZE = 20

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.snake_head = self.segments[0]

    def create_snake(self):
        x_coord = 0
        for _ in range(3):
            segment = Turtle(shape="square")
            segment.color("white")
            segment.penup()
            segment.goto(x=x_coord, y=0)
            self.segments.append(segment)
            x_coord -= 20

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            self.segments[seg_num].goto(self.segments[seg_num - 1].pos())
        self.segments[0].forward(SEGMENT_SIZE)

    def up(self):
        self.snake_head.setheading(90)

    def down(self):
        self.snake_head.setheading(270)

    def left(self):
        self.snake_head.setheading(180)

    def right(self):
        self.snake_head.setheading(0)
