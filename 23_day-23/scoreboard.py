from turtle import Turtle
import init



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color(init.SCOREBOARD_COLOR)
        self.level = 1
        self.setposition(x=(init.SCREEN_WIDTH / -2) + 10, y=(init.SCREEN_HEIGHT / 2) - 40)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", align="left", font=init.SCOREBOARD_FONT)


    def raise_score(self):
        self.level += 1
        self.update_scoreboard()


    def game_over(self):
        self.home()
        self.write(arg="GAME OVER!", align="center", font=init.SCOREBOARD_FONT)
