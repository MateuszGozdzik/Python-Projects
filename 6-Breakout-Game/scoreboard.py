from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 430)
        self.score = -1
        self.add_point()

    def add_point(self):
        self.score += 1
        self.clear()
        self.write(
            f"Score: {self.score}",
            move=False,
            align="center",
            font=("Arial", 30, "bold"),
        )

    def game_over(self):
        self.goto(0, 0)
        self.write(
            f"Game Over.", move=False, align="center", font=("Arial", 30, "bold")
        )
        self.goto(0, -40)
        self.write(
            f"You've scored {self.score} points!",
            move=False,
            align="center",
            font=("Arial", 30, "bold"),
        )
