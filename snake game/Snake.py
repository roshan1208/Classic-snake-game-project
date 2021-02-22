from turtle import Turtle

POSITION = [(0, 0), (-20, 0), (-40, 0)]
COLOR = ['red', 'white', 'white']
UP = 90
DOWN = 270
LEFT = 0
RIGHT = 180


class Snake:
    def __init__(self):

        self.my_turtle = []
        self.create_snake()
        self.snake_head = self.my_turtle[0]

    def create_snake(self):
        for pos in POSITION:
            turtles = Turtle('square')
            turtles.penup()
            turtles.speed('fastest')
            turtles.color('white')
            turtles.goto(pos)
            self.my_turtle.append(turtles)

    def move_up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(90)

    def move_down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(270)

    def move_right(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(0)

    def move_left(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(180)

    def move(self):
        for i in range(len(self.my_turtle) - 1, 0, -1):
            x, y = self.my_turtle[i - 1].pos()
            self.my_turtle[i].goto(x, y)
        self.my_turtle[0].forward(20)

    def extent(self):
        turtles = Turtle('square')
        turtles.penup()
        turtles.speed('fastest')
        turtles.color('white')
        x, y = self.my_turtle[-1].position()
        turtles.goto(x, y)
        self.my_turtle.append(turtles)

    def back_to_screen(self):
        x, y = self.snake_head.position()
        if (self.snake_head.heading() == 0) and (abs(x-300)< 5):
            self.snake_head.goto(-x, y)
            self.snake_head.setheading(0)
        elif (self.snake_head.heading() == 180) and (abs(x-300) > 595):
            self.snake_head.goto(-x, y)
            self.snake_head.setheading(180)
        elif (self.snake_head.heading() == 90) and (abs(y-300)< 5):
            self.snake_head.goto(x, -y)
            self.snake_head.setheading(90)
        elif (self.snake_head.heading() == 270) and (abs(y-300) > 595):
            self.snake_head.goto(x, -y)
            self.snake_head.setheading(270)
        else:
            self.snake_head.goto(x, y)


