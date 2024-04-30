from turtle import Turtle


class LivesBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.lives = 5
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(-300, 300)
        self.update_lives_board()

    def update_lives_board(self):
        if self.lives > 1:
            self.write(f"Lives: {self.lives}", align="right", font=("Courier", 24, "normal"))
        else:
            self.write(f"Life: {self.lives}", align="right", font=("Courier", 24, "normal"))

    def update_lives(self):
        self.lives -= 1
        self.clear()
        self.update_lives_board()