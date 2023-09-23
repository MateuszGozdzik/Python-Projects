from turtle import Turtle
import random
from screen import screen

DIRECTIONS = [45, 135]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(0, -360)
        screen.update()
        self.setheading(random.choice(DIRECTIONS))

    def move(self):
        self.forward(20)
        screen.update()
