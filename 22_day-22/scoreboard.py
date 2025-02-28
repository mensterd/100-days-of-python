from turtle import Turtle
import init

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color(init.SCOREBOARD_COLOR)
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0

        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(-100,200)
        self.write(arg=self.l_score, align="center", font=init.SCOREBOARD_FONT)
        self.goto(100,200)
        self.write(arg=self.r_score, align="center", font=init.SCOREBOARD_FONT)


    def l_point(self, points=1):
        self.l_score += points
        self.update_scoreboard()
        return self.l_score


    def r_point(self, points=1):
        self.r_score += points
        self.update_scoreboard()
        return self.r_score