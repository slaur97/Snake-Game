from turtle import Turtle
dir="C:/Users/Laurentiu/Desktop/snake game"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(x=0,y=260)
        self.write(f"Scor:{self.score}  High-score:{self.read_txt_score()}",align="center",font=("Arial", 24, "normal"))
        self.hideturtle()
    def increase_score(self):
        self.score+=1
        self.clear()
        self.write(f"Scor:{self.score}  High-score:{self.read_txt_score()}",align="center",font=("Arial", 24, "normal"))
    def game_over(self):
        self.goto(x=0,y=0)
        self.write("Game Over",align="center",font=("Arial", 24, "normal"))
    def read_txt_score(self):
        with open(dir+'/highscore.txt','r') as txtFile:
            read=txtFile.read()
            return read
    def write_txt_score(self,new_score):
        with open(dir+'/highscore.txt','w') as txtFile:
            txtFile.write(str(new_score))

    def add_new_high_score(self):
        self.clear()
        self.write(f"Scor:{self.score}  High-score:{self.read_txt_score()}",align="center",font=("Arial", 24, "normal"))