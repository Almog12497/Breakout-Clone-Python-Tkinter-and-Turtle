from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.speed("fastest")
        self.pu()
        self.ht()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-300,190)
        self.write(self.score, align = "center" , font = ("Courier", 80, "normal"))

    def point(self):
        self.score += 1
        self.update_scoreboard()
    
    def win(self):
        self.goto(0,0)
        self.write("YOU WIN!", align = "center" , font = ("Courier", 80, "normal"))
    
    def lose(self):
        self.goto(0,0)
        self.write("GAME OVER", align = "center" , font = ("Courier", 80, "normal"))
    
