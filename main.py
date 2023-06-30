from turtle import Turtle, Screen
from screen_setup import Screen_Setup
from paddles import Paddles, Paddle2
from ball import Ball
import time

screen = Screen()
screen.listen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)
tim = Turtle()
tim.hideturtle()
tim.color("white")
tim.write("Click Spacebar to Start!!", align="center", font=20)
screen_setup = Screen_Setup()
paddle1 = Paddles()
paddle2 = Paddle2()
ball = Ball()
screen.update()


def game_starts():
    game_on = True
    while game_on:
        tim.clear()
        screen.onkey(paddle1.move_up, "Up")
        screen.onkey(paddle1.move_down, "Down")
        screen.onkey(paddle2.move_up, "w")
        screen.onkey(paddle2.move_down, "s")
        ball.move_ball()
        if (-55 < ball.ycor() - paddle1.ycor() < 55) and 400 > ball.xcor() > 370:
            if ball.heading() == 45:
                ball.seth(135)
            elif ball.heading() == 315:
                ball.seth(225)
            ball.move_speed += 0.01

        if (-55 < ball.ycor() - paddle2.ycor() < 55) and -400 < ball.xcor() < -370:
            if ball.heading() == 135:
                ball.seth(45)
            elif ball.heading() == 225:
                ball.seth(315)
            ball.move_speed += 0.01

        if ball.xcor() > 400:
            screen_setup.user1_point()
            ball.move_speed = 0.3
            if screen_setup.score1 < 13:
                ball.goto(0, 0)
                paddle1.goto(380, 0)
                paddle2.goto(-380, 0)
                screen.update()
                time.sleep(2)
            else:
                tim.write("Left User Wins!!", align="center", font=20)
                game_on = False
                break
        elif ball.xcor() < -400:
            screen_setup.user2_point()
            ball.move_speed = 0.3
            if screen_setup.score1 < 13:
                ball.goto(0, 0)
                paddle1.goto(380, 0)
                paddle2.goto(-380, 0)
                screen.update()
                time.sleep(2)
            else:
                tim.write("Right User Wins!!", align="center", font=20)
                game_on = False
                break

        screen.update()


screen.onkey(game_starts, "space")

screen.exitonclick()
