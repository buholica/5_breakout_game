from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(300, 300)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score {self.score}", align="right", font=("Courier", 24, "normal"))

    def update_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()