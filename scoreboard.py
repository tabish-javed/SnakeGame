from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Monospace', 10, 'normal')


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setposition(-250, 270)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", move=False,
                   align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", move=False,
                   align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
