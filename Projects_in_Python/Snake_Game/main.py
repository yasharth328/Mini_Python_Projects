import time
from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
screen.listen()

food = Food()
sybyll = Snake(3)
score = Scoreboard()

screen.onkey(sybyll.up, "Up")
screen.onkey(sybyll.down, "Down")
screen.onkey(sybyll.goright, "Right")
screen.onkey(sybyll.goleft, "Left")

game_is_on = True
while game_is_on:
    sybyll.move()
    screen.update()
    time.sleep(0.1)

    for part in sybyll.snake[1:]:
        if sybyll.snake[0].distance(part) < 10:
            game_is_on = False
            score.gameover()

    if sybyll.snake[0].distance(food) < 15:
        score.increase()
        sybyll.gotfood()
        food.refresh()

    if sybyll.snake[0].xcor() > 280 or sybyll.snake[0].xcor() < -280 or \
            sybyll.snake[0].ycor() > 260 or sybyll.snake[0].ycor() < -280:
        game_is_on = False
        score.gameover()

screen.exitonclick()
