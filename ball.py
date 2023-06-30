from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.up()
        self.setheading(45)
        self.move_speed = 0.2

    def move_ball(self):
        self.forward(self.move_speed)
        if self.heading() == 45 and self.ycor() > 290:
            self.seth(-45)
        elif self.heading() == 315 and self.ycor() < -290:
            self.seth(45)
        elif self.heading() == 135 and self.ycor() > 290:
            self.seth(225)
        elif self.heading() == 225 and self.ycor() < -290:
            self.seth(135)

