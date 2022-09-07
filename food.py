from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        """Create a Food subclass inheriting Turtle Class including all it's objects and"
        "adding additional attributes and methods"""
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Places food for snake as a turtle object randomly between given cordinates."""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
