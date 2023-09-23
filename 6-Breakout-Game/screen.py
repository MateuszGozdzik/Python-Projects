from turtle import Screen, Turtle


screen = Screen()
screen.bgcolor("black")
screen.title("BREAKOUT")
screen.setup(width=1600, height=1000)
screen.tracer(0)


class Painter(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.goto(-775, -475)
        self.pencolor("white")
        self.pensize(10)

    def draw_background(self):
        """Draws background for game"""
        self.pendown()

        self.goto(-775, 475)
        self.pensize(20)
        self.goto(775, 475)
        self.pensize(10)
        self.goto(775, -475)

        screen.update()
