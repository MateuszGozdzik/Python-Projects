from turtle import Turtle
from screen import screen


SPEED = 100


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=15)
        self.color("orange")
        self.goto(0, -400)
        screen.update()

    def add_segment(self, position):
        new_segment = Turtle("square")

        self.segments.append(new_segment)

    def go_left(self):
        """Paddle goes left"""
        if self.xcor() > -650:
            self.setheading(180)
            self.forward(SPEED)
            screen.update()

    def go_right(self):
        """Paddle goes right"""
        if self.xcor() < 650:
            self.setheading(0)
            self.forward(SPEED)
            screen.update()
