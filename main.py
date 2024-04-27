from turtle import Screen
from paddle import Paddle
from ball import Ball
from wall import Wall
import time

screen = Screen()
screen.setup(width=1000, height=700)
screen.bgcolor("black")
screen.title("Breakout Game")
# screen.tracer(0)

paddle = Paddle((0, -320))
ball = Ball()
wall = Wall()

screen.listen()
screen.onkeypress(paddle.move_right, "Right")
screen.onkeypress(paddle.move_left, "Left")

game_on = True
while game_on:
    screen.update()
    ball.move()

    # Detect collision with left and right sides
    if ball.xcor() > 480 or ball.xcor() < -480:
        ball.bounce_x()

    # Detect collision with wall
    for row in wall.container_of_rows:
        for one_wall in row:
            for brick in one_wall:
                if ball.distance(brick) < 35:
                    ball.bounce_y()


    # Detect collision with top
    # if ball.ycor() > 310:
    #     ball.bounce_y()

    # Detect collision with bottom
    if ball.ycor() < -310:
        ball.reset()

screen.exitonclick()
