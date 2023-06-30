from turtle import Turtle


class Paddles(Turtle):

    def __init__(self):
        super().__init__()
        self.make_paddle1()

    def make_paddle1(self):
        self.goto(380, 0)
        self.seth(90)
        self.color("white")
        self.shape("square")
        self.up()
        self.shapesize(stretch_wid=1, stretch_len=5)

    def move_up(self):
        if self.ycor() < 245:
            self.seth(90)
            self.forward(20)

    def move_down(self):
        if self.ycor() > -245:
            self.seth(270)
            self.forward(20)


class Paddle2(Paddles):

    def __init__(self):
        super().__init__()
        self.goto(-380, 0)
