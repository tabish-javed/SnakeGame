from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Monospace', 10, 'normal')


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        """Code above creates Scoreboard class inheriting from Turtle class.
        and add more functions/attributes to it."""
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setposition(-250, 270)
        self.score = 0
        self.update_score()

    def update_score(self):
        """Display/update score on top left corner of the screen"""
        self.write(f"Score: {self.score}", move=False,
                   align=ALIGNMENT, font=FONT)

    def game_over(self):
        """Display 'GAME OVER' message on center of the screen"""
        self.goto(0, 0)
        self.write("GAME OVER!", move=False,
                   align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increment score attribute by 1 each time this functions is called,
        and clear the previous score displayed and overwrite new score."""
        self.score += 1
        self.clear()
        self.update_score()
