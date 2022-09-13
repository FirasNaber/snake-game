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

game_over = False
while not game_over:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.snake_head.distance(food) < 15:
        food.refresh()
        scoreboard.score += 1
        scoreboard.refresh()

screen.exitonclick()
