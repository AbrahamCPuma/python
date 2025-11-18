from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Calibri', 18, 'normal')
FILE_PATH = "D:/python/learningbasicpy/snake_game/data.txt"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.update_scoreboard()
        self.hideturtle()
        
    def update_scoreboard(self):
        self.clear()
        with open(FILE_PATH,mode="r") as data:
            self.highscore = int(data.read())
        self.write(f"Score: {self.score} High Score: {self.highscore}", False, align= ALIGNMENT, font= FONT)
     
        
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


    def reset(self):
        if self.score > self.highscore:
            with open(FILE_PATH,mode="w") as data:
                data.write(f"{self.score}")
        self.score = 0
        self.update_scoreboard()
