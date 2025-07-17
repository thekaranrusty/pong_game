from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
score = Scoreboard()

screen.bgcolor("black")
screen.setup(width= 800, height= 600)
screen.title("Ping Pong")
screen.tracer(0)

screen.listen()

screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_on = True
score_p1 =0
score_p2 =0
delay = 0.1
while game_on:
    screen.update()
    time.sleep(delay)
    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.bounce_y()
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320 or
            ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()
        delay -= 0.005

    if ball.xcor() > 370 :
        ball.refresh()
        score.score_refresh_p1()
        score_p1 += 1
        delay = 0.1
        if score_p1 == 5 :
            score.game_over("Player 1")
            game_on = False
    if ball.xcor() < -370 :
        ball.refresh()
        score.score_refresh_p2()
        score_p2 += 1
        delay = 0.1
        if score_p2 == 5:
            score.game_over("Player 2")
            game_on = False
    ball.move()

print("Game Over")

screen.exitonclick()