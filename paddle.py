from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(1, 9)
        self.setheading(0)
        self.color("white")
        self.goto(position)

    def move_right(self):
        self.forward(30)

    def move_left(self):
        self.backward(30)
