from turtle import Turtle
import copy

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self) -> None:
        self.snake = []
        self.create_snake()
        self.plot_snake()
        self.head = self.snake[0]  # Create a head attribute with 'snake[0]' content.

    def create_snake(self):
        """Create snake body (as list) with three turtle objects to start with."""
        for number_of_boxes in range(3):
            # This calls add_boxes function three times
            self.add_boxes(number_of_boxes)

    def plot_snake(self):
        """Sets starting position of snake (a list of three objects) at screen cordinates"""
        for i in range(0, len(self.snake)):
            self.snake[i].goto(-20 * i, 0)

    def add_boxes(self, number_of_boxes):
        """Create a list of boxes (snake segments) objects"""
        box = Turtle(shape="square")
        box.color("white")
        box.shapesize(1)
        box.penup()
        self.snake.append(box)

    def extend(self):
        """Add a new segment/box at the end of snake tail (list)"""
        self.add_boxes(self.snake[-1].position())
        """This calls add_boxes function to append a box at the very last of the list"""

    def move(self):
        """Move the snake body (all three objects/boxes) horizontally """
        for box_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[box_num - 1].xcor()
            new_y = self.snake[box_num - 1].ycor()
            self.snake[box_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    """All 4 methods below doesn't allow snake to move backward if it's heading to forward
    and vice versa..."""

    def up(self):
        """Doesn't allow head/snake to go back opposit to direction it's moving in, i.e.
        this code below; doesn't allow head to go up if it's heading down."""
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
