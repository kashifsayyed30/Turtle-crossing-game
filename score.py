from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.penup()
        self.goto(-280, 260)
        self.update_score()

    def update_score(self):
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increment_level(self):
        self.level += 1
        self.clear()
        self.update_score()

    def game_over_text(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)
