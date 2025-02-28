from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
from time import sleep
import init

#https://docs.python.org/3/library/turtle.html#

screen = Screen()
screen.screensize(canvwidth=init.SCREEN_WIDTH, canvheight=init.SCREEN_HEIGHT)
screen.bgcolor(init.SCREEN_COLOR)
screen.title("Pong!")
# Hides animation on the screen
screen.tracer(0)


right_paddle = Paddle(start_position=(350,0))
left_paddle = Paddle(start_position=(-350,0))
ball = Ball()
scoreboard = ScoreBoard()

game_is_on = True

screen.listen()

def end_game():
    global game_is_on
    game_is_on = False


screen.onkey(right_paddle.move_up, key="Up")
screen.onkey(right_paddle.move_down, key="Down")

screen.onkey(left_paddle.move_up, key="w")
screen.onkey(left_paddle.move_down, key="s")

# Exists the while loop
screen.onkey(end_game, key="q")

direction = 1

while game_is_on:

    ball.move(direction)
    screen.update()
    sleep(0.1)

    # Check for collision with screen borders (top and bottom)
    if ball.ycor() >= 300 or ball.ycor() <= -300:
        ball.bounce_y()

    # Check dor collision with paddle
    if (ball.distance(left_paddle) < 50 and ball.xcor() < -320) or (ball.distance(right_paddle) < 50 and ball.xcor() > 320):
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() >= 380:
        ball.reset_position()
        scoreboard.l_point()
        print("left scores")

    # Detect L paddle misses
    if ball.xcor() <= -380:
        ball.reset_position()
        scoreboard.r_point()
        print("Right scores")

screen.exitonclick()