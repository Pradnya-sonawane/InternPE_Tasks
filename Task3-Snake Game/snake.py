from turtle import Turtle,Screen
import random
import time

SNAKE_COLOR = "#86E5FF"
FOOD_COLOR = "#FFC93C"
BG_COLOR = "#000000"
DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
POS =  [(0, 0),(-20, 0),(-40, 0)]#for first 3 segments
SIZE = 700
BOUNDARY = (SIZE/2)-5

screen = Screen()
screen.setup(width=SIZE, height=SIZE)
screen.title("The Snake Game")
screen.bgcolor(BG_COLOR)
screen.tracer(0) #for turning animation on or off


class Snake:
    def __init__(self):
        self.turtle_list = []
        self.body()
        self.head = self.turtle_list[0]

    def body(self):
        for i in POS:
            self.add_segment(i)

    def add_segment(self, p):
        t=Turtle('square')
        t.color(SNAKE_COLOR)
        t.penup()
        t.goto(p)
        self.turtle_list.append(t)

    def move(self):
        #give positioning in reverse direction
        for t in range(len(self.turtle_list)-1, 0, -1):
            x= self.turtle_list[t-1].xcor()
            y= self.turtle_list[t-1].ycor()
            self.turtle_list[t].goto(x, y)
        self.head.forward(DIST)

    def extend_snake(self):
        n = self.turtle_list[-1].position()
        self.add_segment(n) 

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)



class Food(Snake):
    def __init__(self):
        super().__init__()
        self.food = Turtle('circle')
        self.food.penup()
        self.food.color(FOOD_COLOR)
        self.food.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.food.speed('fastest')
        self.refresh_food()

    def refresh_food(self):
        fx = random.randint(-280,330)
        fy = random.randint(-330,330)
        self.food.goto(fx, fy)

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0,310)
        self.score = 0
        self.write(f"Score:{self.score}")
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font = ("Ariel", 24,"normal"))

    def increase_score(self):
        self.score +=1
        self.update_score()
    def final_score(self):
        self.goto(0,0)
        self.color('red')
        self.write(f"Game Over! With Score {self.score}", align="center", font=("Ariel", 32, "normal"))


f = Food()
score = ScoreBoard()
screen.listen() #for listening keyboard events
screen.onkey(f.up, "Up")
screen.onkey(f.down, "Down")
screen.onkey(f.left, "Left")
screen.onkey(f.right, "Right")


flag = True
while flag:
    screen.update()
    f.move()
    time.sleep(0.1)

    #............................................1.checking collision of food......................................
    if f.head.distance(f.food)<15:
        f.refresh_food()
        f.extend_snake()
        score.increase_score()

    #......................................2.checking collision of snake with wall..................................
    if f.head.xcor() > BOUNDARY or f.head.xcor() < -BOUNDARY or f.head.ycor() > BOUNDARY or f.head.ycor() < -BOUNDARY:
         flag = False
         score.final_score()
    
    #....................................3.ckecking collision of snake with it's body...............................
    for t in f.turtle_list:
        if f.head==t:
            pass
        elif f.head.distance(t)<10:
            flag = False
            score.final_score()

screen.exitonclick()






