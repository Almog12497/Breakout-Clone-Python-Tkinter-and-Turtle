from turtle import Turtle
from random import randint, choice

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.pu()
        self.speed("fastest")
        # self.x_move = randint(-10,10)
        # self.y_move = randint(-10,10)
        self.x_move = choice([-5,5])
        self.y_move = -5
        self.goto(x=0,y=-20)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset(self):
        self.goto(0,-20)
        # self.x_move = randint(-10,10)
        # self.y_move = randint(-10,10)
        self.x_move = choice([-5,5])
        self.y_move = -5