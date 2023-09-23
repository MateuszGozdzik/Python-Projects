"""Breakout Game"""
import time
from screen import screen, Painter
from paddle import Paddle
from blocks import BLOCKS
from scoreboard import ScoreBoard
from ball import Ball


class Gamer:
    def __init__(self):
        self.BLOCKS = BLOCKS
        self.GAME_IS_ON = True
        self.painter = Painter()
        self.painter.draw_background()
        self.scoreboard = ScoreBoard()
        self.paddle = Paddle()
        self.ball = Ball()
        self.screen = screen
        self.screen.listen()
        self.screen.onkeypress(self.paddle.go_left, "Left")
        self.screen.onkeypress(self.paddle.go_right, "Right")

    def check_for_paddle_collision(self):
        if self.ball.distance(self.paddle) < 155 and self.ball.ycor() < -410:
            if self.ball.xcor() < self.paddle.xcor():
                self.ball.setheading(135)
            else:
                self.ball.setheading(45)
            self.ball.move()
            self.ball.move()

    def check_for_wall_collision(self):
        # * Top
        if self.ball.ycor() > 450:
            if self.ball.heading() == 45:
                self.ball.setheading(315)
            else:  # ball.heading() == 135
                self.ball.setheading(225)

        # * Right
        if self.ball.xcor() > 765:
            if self.ball.heading() == 45:
                self.ball.setheading(135)
            else:  # ball.heading() == 315
                self.ball.setheading(225)

        # * Left
        if self.ball.xcor() < -765:
            if self.ball.heading() == 135:
                self.ball.setheading(45)
            else:  # ball.heading() == 225
                self.ball.setheading(315)

    def check_for_block_collision(self):
        for block in self.BLOCKS.copy():
            if self.ball.distance(block) < 80:
                block.hideturtle()
                BLOCKS.remove(block)
                screen.update()

                self.scoreboard.add_point()
                self.ball.setheading(360 - self.ball.heading())
                break

    def check_for_game_over(self):
        if self.ball.ycor() < -450:
            self.GAME_IS_ON = False
            self.scoreboard.game_over()

        elif len(BLOCKS) == 0:
            self.GAME_IS_ON = False
            self.scoreboard.game_over()

    def game(self):
        while self.GAME_IS_ON:
            self.ball.move()
            time.sleep(0.05)
            self.check_for_paddle_collision()
            self.check_for_block_collision()
            self.check_for_wall_collision()
            self.check_for_game_over()
