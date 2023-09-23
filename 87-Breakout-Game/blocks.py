from turtle import Turtle
from screen import screen
import random


color_list = ["red", "blue", "orange", "green", "purple", "yellow"]
rows = []


class Block(Turtle):
    def __init__(self, color):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=3, stretch_len=7)
        self.penup()
        screen.update()


class Row:
    def __init__(self, y_cor, color):
        self.blocks = []

        for i in range(10):
            new_block = Block(color)
            new_block.goto(-675 + i * 150, y_cor)
            self.blocks.append(new_block)


rows.append(Row(300, "red"))
rows.append(Row(200, "blue"))
rows.append(Row(100, "green"))

# BLOCKS = [block for block in row.blocks for row in rows]
blocks = []
for row in rows:
    for block in row.blocks:
        blocks.append(block)
