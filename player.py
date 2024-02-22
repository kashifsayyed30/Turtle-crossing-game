from turtle import Turtle

START_POS = (0, -280)
MOVE_DIST = 10
FINISH_LINE_y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("red")
        self.shapesize(1)
        self.penup()
        self.goto(START_POS)
        self.setheading(90)

    def move_up(self):
        self.forward(MOVE_DIST)

    def at_finish(self):
        if self.ycor() > FINISH_LINE_y:
            return True
        else:
            return False

    def go_at_start(self):
        self.goto(START_POS)
