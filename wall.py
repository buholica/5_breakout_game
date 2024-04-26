from turtle import Turtle

STARTING_POSITIONS = [(-430, 100), (-300, 100), (-170, 100)]
COLORS = ["purple", "blue", "green", "yellow", "orange", "red"]
CONTAINER_WIDTH = 900
CONTAINER_HEIGHT = 250


class Wall(Turtle):
    def __init__(self):
        super().__init__()
        self.walls = []
        self.bricks_row = []
        self.add_wall()
        self.num_walls = len(COLORS)

    def create_brick(self, x_cord, y_cord, color):
        new_brick = Turtle("square")
        new_brick.shapesize(1, 6)
        new_brick.color(color)
        new_brick.penup()
        new_brick.speed("fastest")
        new_brick.goto(x=x_cord, y=y_cord)
        return new_brick

    def add_row(self, x_cord, y_cord, color):
        row_bricks = []
        for brick in range(7):
            new_brick = self.create_brick(x_cord, y_cord, color)
            row_bricks.append(new_brick)
            x_cord += 140
        return row_bricks

    def add_wall(self):
        x_cord = -425
        y_cord = 90
        color = 0
        self.walls.append(self.add_row(x_cord, y_cord, COLORS[color]))
        y_cord += 30
        for row in range(1, 6):
            x_cord = -425
            color += 1
            self.walls.append(self.add_row(x_cord, y_cord, COLORS[color]))
            y_cord += 30
        print(len(self.walls))

