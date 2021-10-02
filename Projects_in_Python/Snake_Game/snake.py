from turtle import Turtle, Vec2D


class Snake:

    def __init__(self, snakelen):
        self.snakelen = snakelen
        self.snake = []
        pos = Vec2D(0, 0)
        for part in range(self.snakelen):
            snakepart = Turtle("square")
            snakepart.penup()
            snakepart.setpos(pos)
            pos += Vec2D(-20, 0)
            snakepart.color("white")
            self.snake.append(snakepart)

    def move(self):
        for seg_num in range(len(self.snake) - 1, 0, -1):
            pos_seg = self.snake[seg_num - 1].pos()
            self.snake[seg_num].goto(pos_seg)
        self.snake[0].forward(20)

    def up(self):
        self.snake[0].setheading(90)

    def down(self):
        self.snake[0].setheading(270)

    def goleft(self):
        self.snake[0].setheading(180)

    def goright(self):
        self.snake[0].setheading(0)

    def gotfood(self):
        snakepart = Turtle("square")
        snakepart.color("white")
        snakepart.penup()
        self.snake.append(snakepart)