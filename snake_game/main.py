from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)  # turn the tracer off

initial_positions = [(0,0), (-20,0), (-40,0)]
snake_segments = [] 

for position in initial_positions:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    snake_segments.append(new_segment)

screen.update()

game_is_in_progress = True

while game_is_in_progress:
    screen.update()
    time.sleep(0.1)
    
    for i in range(len(snake_segments)-1, 0, -1):
        new_x, new_y = snake_segments[i-1].position()
        snake_segments[i].goto(new_x, new_y)
    snake_segments[0].forward(20)
    
screen.exitonclick()