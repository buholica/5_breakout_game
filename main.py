from turtle import Screen
from paddle import Paddle
from ball import Ball
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
wall = Wall()
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
        ball.bounce_y()

    # Detect collision with left and right sides
    if ball.xcor() > 480 or ball.xcor() < -480:
        ball.bounce_x()

    # Detect collision with top
    if ball.ycor() > 310:
        ball.bounce_y()


game_on = True
while game_on:
    screen.update()
    time.sleep(0.01)
    ball.move()

    # Detect collision with paddle
    detect_collision_with_paddle()

    # Detect collision with sides
    detect_collision_with_sides()


screen.exitonclick()
