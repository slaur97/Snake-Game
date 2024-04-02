from turtle import Turtle
move_distance=20
poz_start=[(0,0),(-20,0),(-40,0)]
Up=90
Down=270
Left=180
Right=0
class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]
        
    
    def create_snake(self):
        for squere in poz_start:
            self.add_segments(squere)
           
    def add_segments(self,pozition):
        tim=Turtle(shape="square")
        tim.penup()
        tim.color('white')
        tim.goto(pozition)
        self.segments.append(tim)
    def extend(self):
        self.add_segments(self.segments[-1].position())


    def move(self):
        for seg_num in range(len(self.segments)-1 ,0,-1):
            new_x=self.segments[seg_num-1].xcor()
            new_y=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(move_distance)
        

    def up(self):
        if self.head.heading() != Down:
            self.head.setheading(Up)
    def left(self):
        if self.head.heading() != Right:
            self.head.setheading(Left)
    def down(self):
        if self.head.heading() != Up:
            self.head.setheading(Down)
    def right(self):
        if self.head.heading() != Left:
            self.head.setheading(Right)
