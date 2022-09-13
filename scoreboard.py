from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.setpos(0, 265)
        self.refresh()
        self.hideturtle()

    def refresh(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.penup()
        self.setpos(0, 0)
        self.color("white")
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)
