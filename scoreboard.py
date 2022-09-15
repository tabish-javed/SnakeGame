from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Monospace', 10, 'normal')  # A tuple constant


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        """Code above creates Scoreboard class inheriting from Turtle class.
        and add more functions/attributes to it."""
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.high_score = self.read_data()
        self.update_score()

    def update_score(self):
        """Display/update score on top left corner of the screen"""
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}",
                   align=ALIGNMENT, font=FONT)

    def reset(self):
        """Reset current score to zero and update high_score."""
        if self.score > self.high_score:
            self.high_score = self.score
        self.write_data()
        self.score = 0
        self.update_score()

    def increase_score(self):
        """Increment score attribute by 1 each time this functions is called,
        and clear the previous score displayed and overwrite new score."""
        self.score += 1
        self.update_score()

    def read_data(self):
        """Read the last high_score from file."""
        with open("high_score.txt", mode="r") as data:
            self.high_score = int(data.read())
        return self.high_score

    def write_data(self):
        """Write the high_score to file."""
        with open("high_score.txt", mode="w") as data:
            data.write(str(self.high_score))
