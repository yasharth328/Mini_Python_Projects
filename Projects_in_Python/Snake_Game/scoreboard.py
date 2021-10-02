from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()
        self.sety(270)
        self.pencolor("grey")
        self.score = 0
        self.writescore()

    def increase(self):
        self.score += 1
        self.writescore()

    def writescore(self):
        self.clear()
        scorewriting = f"____________________ ~ Score: {self.score} ~ ____________________"
        self.write(scorewriting, align="center", font=("Copperplate", 16, "normal"))

    def gameover(self):
        self.sety(0)
        self.write("GAME OVER", align="center", font=("Copperplate", 30, "normal"))
