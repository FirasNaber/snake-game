import time
from food import Food
from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.score += 1
        scoreboard.refresh()
        snake.extend()

    # Detect collision with self
    for seg in snake.segments:
        if snake.head.distance(seg) < 10 and seg != snake.segments[0]:
            game_on = False
            scoreboard.game_over()

    # Detect collision with walls
    if snake.head.xcor() < -290 or snake.head.xcor() > 280 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
        game_on = False
        scoreboard.game_over()

screen.exitonclick()
