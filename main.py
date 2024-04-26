from turtle import Screen
from paddle import Paddle
from ball import Ball
from wall import Wall
import time

screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("Breakout Game")
# screen.tracer(0)

paddle = Paddle((0, -270))
ball = Ball()
wall = Wall()

screen.listen()
screen.onkeypress(paddle.move_right, "Right")
screen.onkeypress(paddle.move_left, "Left")

game_on = True
while game_on:
    # screen.update()
    ball.move()

    if ball.xcor() > 480 or ball.xcor() < -480:
        ball.bounce_x()

    if ball.distance(paddle) < 50 or ball.ycor() > 270:
        ball.bounce_y()

    if ball.ycor() < -270:
        ball.reset()

screen.exitonclick()
