from turtle import Turtle,Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title("my snake game")
screen.tracer(0)

scoreboard=Scoreboard()
snake=Snake()
food =Food()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

start=True
while start:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #detect colision with food
    if snake.head.distance(food) < 15:
        snake.extend()
        scoreboard.increase_score()
        food.refresh()
    #detect colision with wall
    if snake.head.xcor() >290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        start=False
        scoreboard.game_over()

    if int(scoreboard.score) > int(scoreboard.read_txt_score()):
        scoreboard.write_txt_score(scoreboard.score)
        scoreboard.add_new_high_score()
    #detect colision with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            start=False
            scoreboard.game_over()
    
screen.exitonclick()