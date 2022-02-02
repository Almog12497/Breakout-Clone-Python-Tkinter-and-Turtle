from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from brick import Brick
import time
import random

COLORS = ["blue", "red", "green"]
screen = Screen()
screen.title("Breakout")
screen.tracer()
screen.setup(width = 800, height = 600, )
screen.bgcolor("black")

paddle = Paddle(x_pos=0, y_pos=-250, color="white")
scoreboard = Scoreboard()

bricks = []
for i in range(10):
    for j in range(5):
        brick = Brick(-300+i*70, 150-j*30, color=random.choice(COLORS))
        bricks.append(brick)

ball = Ball()

screen.listen()
screen.onkey(paddle.left, "Left")
screen.onkey(paddle.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.016)
    ball.move()

    #Detect collision with wall
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()
    
    #Detect collision with celling
    if ball.ycor() > 280 :
        ball.bounce_y()

    #Detect failure
    if ball.ycor() < -260:
        game_is_on = False
        scoreboard.lose()
        ball.reset()
        time.sleep(2)
    
    #Detect collision with bricks
    for brick in bricks:
        if brick.distance(ball) < 40:
            brick.destroy()
            ball.bounce_y()
            scoreboard.point()

    #Detect collision with paddle
    if paddle.distance(ball) < 50 and ball.ycor() < - 230:
        ball.bounce_y()
    
    if scoreboard.score == len(bricks) :
        game_is_on = False
        scoreboard.win()




screen.exitonclick()