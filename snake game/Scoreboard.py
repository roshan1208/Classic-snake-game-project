from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as file:
            self.highestscore = int(file.read())
        self.speed('fastest')
        self.color('white')
        self.penup()
        self.goto(-160, 260)
        self.hideturtle()
        self.write(f'Score :{self.score}', align=ALIGNMENT, font=FONT)
        self.high_tur = 0




    def score_update(self):
        self.clear()
        self.score += 1
        self.write(f'Score :{self.score}', align=ALIGNMENT, font=FONT)
        self.goto(-160, 260)

    def highestscore_update(self):
        tur = Turtle()
        tur.hideturtle()
        tur.color('white')
        tur.clear()
        tur.penup()
        tur.goto(150, 260)
        with open('data.txt','r') as file:
            self.highestscore = file.read()
        tur.write(f'Highest Score :{self.highestscore}', align=ALIGNMENT, font=FONT)

        self.high_tur = tur


    def game_over(self):
        with open('data.txt','w') as file:
            file.write(str(self.score))
        self.goto(0, 0)
        self.color('red')
        self.write(f'Game Over', align=ALIGNMENT, font=("Courier", 28, "normal"))
