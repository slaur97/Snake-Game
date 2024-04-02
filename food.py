from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.refresh()
    def refresh(self):
        self.new_x=random.randint(-280,280)
        self.new_y=random.randint(-280,280)
        self.goto(self.new_x,self.new_y)
            