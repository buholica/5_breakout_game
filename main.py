from turtle import Screen
from paddle import Paddle
from ball import Ball
from bricks import Bricks
from wall import Wall
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=1000, height=700)
screen.bgcolor("black")
screen.title("Breakout Game")
screen.tracer(0)

paddle = Paddle()
ball = Ball()
# wall = Wall()
bricks = Bricks()
scoreboard = Scoreboard()
screen.update()

screen.listen()
screen.onkeypress(paddle.move_right, "Right")
screen.onkeypress(paddle.move_left, "Left")


def detect_collision_with_paddle():
    global ball, paddle
    for seg in paddle.segments:
        if ball.distance(seg) < 40:
            ball.bounce_y()


def detect_collision_with_sides():
    global ball
    # Detect collision with bottom
    if ball.ycor() < -310:
        ball.reset()

    # Detect collision with left and right sides
    if ball.xcor() > 480 or ball.xcor() < -480:
        ball.bounce_x()

    # Detect collision with top
    if ball.ycor() > 310:
        ball.bounce_y()


def detect_collision_with_bricks(row_bricks, y_cor):
    for color, brick_list in row_bricks.items():
        for brick in brick_list:
            if ball.ycor() > y_cor and ball.distance(brick) < 50:
                ball.bounce_y()
                brick.hideturtle()
                brick_list.remove(brick)


game_on = True
while game_on:
    screen.update()
    time.sleep(0.01)
    ball.move()

    # Detect collision with paddle
    detect_collision_with_paddle()

    # Detect collision with sides
    detect_collision_with_sides()

    # Detect collision with walls
    detect_collision_with_bricks(bricks.bricks, 40)
    detect_collision_with_bricks(bricks.bricks, 70)
    detect_collision_with_bricks(bricks.bricks, 100)
    detect_collision_with_bricks(bricks.bricks, 130)
    detect_collision_with_bricks(bricks.bricks, 160)
    detect_collision_with_bricks(bricks.bricks, 190)


screen.exitonclick()
