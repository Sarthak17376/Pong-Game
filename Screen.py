from turtle import Turtle

line_maker = Turtle()


def line():
    line_maker.speed("fastest")
    line_maker.hideturtle()
    line_maker.goto(0, 300)
    line_maker.setheading(270)
    line_maker.color("white")
    while line_maker.ycor() > -300:
        line_maker.forward(25)
        line_maker.up()
        line_maker.forward(25)
        line_maker.down()


class Screen_Setup(Turtle):

    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.hideturtle()
        self.goto(0, 200)
        self.score1 = 0
        self.score2 = 0
        self.color("white")
        self.write(f"{self.score1}      {self.score2}", align="center", font=("Stencil", 50, "normal"))
        line()

    def user1_point(self):
        self.clear()
        self.score1 += 1
        self.write(f"{self.score1}      {self.score2}", align="center", font=("Stencil", 50, "normal"))

    def user2_point(self):
        self.clear()
        self.score2 += 1
        self.write(f"{self.score1}      {self.score2}", align="center", font=("Stencil", 50, "normal"))
