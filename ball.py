from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(1, 1)
        self.color("white")
        self.penup()
        self.goto(0, -50)
        self.x_move = 10
        self.y_move = 10
        # self.move_speed = 0.1

    def move(self):
        x_cor = self.xcor() + self.x_move
        y_cor = self.ycor() + self.y_move
        self.goto(x_cor, y_cor)

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1
        # self.move_speed *= 0.9

    def reset(self):
        self.goto(0, -50)
        # self.move_speed = 0.1
        self.bounce_y()
