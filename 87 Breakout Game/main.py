"""Breakout Game"""
import time
from screen import screen, Painter
from paddle import Paddle
from blocks import BLOCKS
from scoreboard import ScoreBoard
from ball import Ball



GAME_IS_ON = True

# Background
painter = Painter()
painter.draw_background()

scoreboard = ScoreBoard()


# Paddle
paddle = Paddle()

screen.listen()
screen.onkeypress(paddle.go_left, "Left")
screen.onkeypress(paddle.go_right, "Right")


# Ball
ball = Ball()
while GAME_IS_ON:

    ball.move()
    time.sleep(0.05)

    #* Collision with Paddles

    if ball.distance(paddle) < 155 and ball.ycor() < -410:
        if ball.xcor() < paddle.xcor():
            ball.setheading(135)
        else:
            ball.setheading(45)
        ball.move()
        ball.move()
        # scoreboard.add_point()

    #* Collision with Walls

        #* Top
    if ball.ycor() > 450:
        if ball.heading() == 45:
            ball.setheading(315)
        else: #ball.heading() == 135
            ball.setheading(225)

        #* Right
    if ball.xcor() > 765:
        if ball.heading() == 45:
            ball.setheading(135)
        else: #ball.heading() == 315
            ball.setheading(225)

        #* Left
    if ball.xcor() < -765:
        if ball.heading() == 135:
            ball.setheading(45)
        else: #ball.heading() == 225
            ball.setheading(315)

    #* Collision with Blocks
    for block in BLOCKS.copy():
        if ball.distance(block) < 80:
            block.hideturtle()
            BLOCKS.remove(block)

            scoreboard.add_point()
            ball.setheading(360 - ball.heading())
            break

    #* Game Over
    if ball.ycor() < -450:
        GAME_IS_ON = False



screen.exitonclick()
