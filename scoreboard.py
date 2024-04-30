from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(250, 300)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}",
                   align="center", font=("Courier", 24, "normal"))

    def update_score(self, point):
        self.score += point
        self.clear()
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.high_score}")