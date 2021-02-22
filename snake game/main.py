from turtle import Screen
import time
from Snake import Snake
from Food import Food
from Scoreboard import ScoreBoard

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(key='Up', fun=snake.move_up)
screen.onkey(key='Down', fun=snake.move_down)
screen.onkey(key='Left', fun=snake.move_left)
screen.onkey(key='Right', fun=snake.move_right)


is_true = True
while is_true:
    screen.update()
    time.sleep(0.2)
    snake.move()
    score.highestscore_update()

    x, y = snake.snake_head.pos()
    if (abs(abs(x) - 300) < 5) or (abs(abs(y) - 300) < 5):
        snake.back_to_screen()

    if snake.snake_head.distance(food) < 15:
        food.update_food()
        snake.extent()
        score.score_update()

    for segment in snake.my_turtle:
        if segment == snake.snake_head:
            pass
        elif snake.snake_head.distance(segment) < 10:
            is_true = False

            score.game_over()


screen.exitonclick()


