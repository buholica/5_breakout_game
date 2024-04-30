from turtle import Turtle


class Message(Turtle):
    def __init__(self):
        super().__init__()
        self.text = ""
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 0)
        self.update_message(self.text)

    def update_message(self, text):
        self.write(f"{text}", align="center", font=("Courier", 28, "bold"))