from turtle import Turtle
import random
HEIGHT = 600
WEIGHT = 600

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed('fastest')
        self.shape('circle')
        self.color('blue')
        self.shapesize(stretch_wid=0.7, stretch_len=0.7)
        self.goto(40, 40)


    def update_food(self):
        ran_x = random.randint(-(WEIGHT/2-30), (WEIGHT/2)-30)
        ran_y = random.randint(-(HEIGHT/2-30), (HEIGHT/2)-30)
        self.speed('fastest')
        self.goto(ran_x, ran_y)