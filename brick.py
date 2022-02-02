from turtle import Turtle

class Brick(Turtle):
    def __init__(self,x_pos,y_pos, color = "white"):
        super().__init__()
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.pu()
        self.shape("square")
        self.color(color)
        self.turtlesize(0.5,2)
        self.speed("fastest")
        self.goto(x = self.x_pos, y = self.y_pos)
    
    def destroy(self):
        self.goto(x=500,y=600)