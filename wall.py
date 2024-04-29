from turtle import Turtle

COLORS = ["purple", "blue", "green", "yellow", "orange", "red"]


class Wall(Turtle):
    def __init__(self):
        super().__init__()
        self.num_walls = 7
        self.container_of_rows = []
        self.wall_length = 6
        self.num_rows = 7
        self.num_walls_in_column = len(COLORS)
        self.num_col = len(COLORS)
        self.create_row_container()

    def create_brick(self, x_cord, y_cord, color):
        """Create a 1-1 brick for making a wall"""
        brick = Turtle("square")
        brick.penup()
        brick.shapesize(1, 1)
        brick.color(color)
        brick.speed("fastest")
        brick.goto(x=x_cord, y=y_cord)
        return brick

    def create_wall(self, x_cord, y_cord, color):
        """Create a wall made of certain amount of bricks"""
        wall = []
        for _ in range(self.wall_length):
            brick = self.create_brick(x_cord, y_cord, color)
            wall.append(brick)
            x_cord += 21
        print(f"The length of wall list: {len(wall)}")
        return wall

    def create_row_container(self):
        """Create a container that has certain amount of rows made of walls"""
        x_cord = -458
        y_cord = 100
        color_index = 0
        for wall in range(self.num_col):
            row = []
            for _ in range(self.num_rows):
                wall = self.create_wall(x_cord, y_cord, COLORS[color_index])
                row.append(wall)
                x_cord += 135

            self.container_of_rows.append(row)
            x_cord = -458
            y_cord += 30
            color_index += 1
        print(f"The length of the container list: {len(self.container_of_rows)}")

    def remove_wall(self, brick):
        for row in self.container_of_rows:
            for wall in row:
                if brick in wall:
                    brick.hideturtle()
                    wall.remove(brick)
                row.remove(wall)
            print(f"The length of row is: {len(row)}.")
