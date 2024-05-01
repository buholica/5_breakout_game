from turtle import Turtle

Y_COR = -310
STARTING_POSITIONS = [(-60, Y_COR), (-40, Y_COR), (-20, Y_COR),
                      (0, Y_COR), (20, Y_COR), (40, Y_COR), (60, Y_COR)]
MOVE_DISTANCE = 40


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_paddle()

    def create_paddle(self):
        for position in STARTING_POSITIONS:
            self.add_segments(position)

    def add_segments(self, position):
        for _ in range(7):
            new_part = Turtle("square")
            new_part.shapesize(1, 1)
            new_part.color("white")
            new_part.penup()
            new_part.setheading(0)
            new_part.goto(position)
            self.segments.append(new_part)

    def move_right(self):
        if self.segments[-1].xcor() + MOVE_DISTANCE <= 450:
            for segment in self.segments:
                segment.forward(MOVE_DISTANCE)

    def move_left(self):
        if self.segments[0].xcor() + MOVE_DISTANCE >= -450:
            for segment in self.segments:
                segment.backward(MOVE_DISTANCE)