from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(x=0,y=260)
        self.write(f"Scor:{self.score}",align="center",font=("Arial", 24, "normal"))
        self.hideturtle()
    def increase_score(self):
        self.score+=1
        self.clear()
        self.write(f"Scor:{self.score}",align="center",font=("Arial", 24, "normal"))
    def game_over(self):
        self.goto(x=0,y=0)
        self.write("Game Over",align="center",font=("Arial", 24, "normal"))
       