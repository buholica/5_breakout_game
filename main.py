from turtle import Screen
from paddle import Paddle
from ball import Ball
from bricks import Bricks
from scoreboard import Scoreboard
from lives import LivesBoard
from message import Message
import time

screen = Screen()
screen.setup(width=1000, height=700)
screen.bgcolor("black")
screen.title("Breakout Game")
screen.tracer(0)

paddle = Paddle()
ball = Ball()
bricks = Bricks()
rows_of_bricks = bricks.bricks
scoreboard = Scoreboard()
lives_board = LivesBoard()
message = Message()
screen.update()


def detect_collision_with_paddle():
    global ball, paddle
    for seg in paddle.segments:
        if ball.distance(seg) < 40:
            ball.bounce_y()


def detect_collision_with_sides():
    global ball
    # Detect collision with bottom
    if ball.ycor() < -310:
        lives_board.update_lives()
        ball.reset()

    # Detect collision with left and right sides
    if ball.xcor() > 480 or ball.xcor() < -480:
        ball.bounce_x()

    # Detect collision with top
    if ball.ycor() > 290:
        ball.bounce_y()


def detect_collision_with_bricks():
    y_cor = 0
    point = 0
    for color, brick_list in rows_of_bricks.items():
        if color == "purple":
            y_cor, point = 40, 1
        elif color == "blue":
            y_cor, point = 80, 2
        elif color == "green":
            y_cor, point = 120, 3
        elif color == "yellow":
            y_cor, point = 160, 4
        elif color == "orange":
            y_cor, point = 200, 5
        elif color == "red":
            y_cor, point = 240, 6

        for brick in brick_list:
            if ball.ycor() > y_cor and ball.distance(brick) < 50:
                ball.bounce_y()
                brick.hideturtle()
                brick_list.remove(brick)
                scoreboard.update_score(point)

        print(f"The {color}_list has {len(brick_list)} values inside.")


game_on = False
start_game = screen.textinput(title="Start to play", prompt='Type "start" to start the game.')

if start_game.lower() == "start":
    game_on = True

while game_on:
    screen.update()
    time.sleep(0.01)
    ball.move()

    screen.listen()
    screen.onkeypress(paddle.move_right, "Right")
    screen.onkeypress(paddle.move_left, "Left")

    # Detect collision with paddle
    detect_collision_with_paddle()

    # Detect collision with sides
    detect_collision_with_sides()

    # Detect collision with walls
    detect_collision_with_bricks()

    # Finish the game
    if lives_board.lives == 0 and scoreboard.score < 147:
        game_on = False
        scoreboard.reset()
        message.update_message("Sorry, you lose!")

    if scoreboard.score >= 147 and lives_board.lives > 0:
        game_on = False
        scoreboard.reset()
        message.update_message("Congratulations! You won the game!")


screen.exitonclick()
