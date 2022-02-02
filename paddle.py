from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,x_pos,y_pos, color = "white"):
        super().__init__()
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.pu()
        self.shape("square")
        self.color(color)
        self.turtlesize(1,5)
        self.speed("fastest")
        self.goto(x = self.x_pos, y = self.y_pos)
    
    def right(self):
        self.x_pos += 40
        self.goto(x = self.x_pos, y = self.y_pos )   

    def left(self):
        self.x_pos -= 40
        self.goto(x = self.x_pos, y = self.y_pos )