from turtle import Turtle

COLORS = ["purple", "blue", "green", "yellow", "orange", "red"]


class Brick(Turtle):
    def __init__(self, x_cor, y_cor, color):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.penup()
        self.shapesize(stretch_wid=1.5, stretch_len=6)
        self.goto(x_cor, y_cor)


class Bricks:
    def __init__(self):
        self.bricks = {}
        self.quantity = 7
        self.create_all_rows()

    def create_row(self, x_cord, y_cord, color):
        row_bricks = []
        for _ in range(self.quantity):
            brick = Brick(x_cord, y_cord, color)
            row_bricks.append(brick)
            x_cord += 135
        return row_bricks

    def create_all_rows(self):
        x_cord = -410
        y_cord = 80
        color_index = 0
        for index, color in enumerate(COLORS):
            self.bricks[color] = self.create_row(x_cord, y_cord, color)
            y_cord += 40
            color_index += 1
            print(f"The length of {color} list is {len(self.bricks[color])}.")