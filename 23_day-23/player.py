from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.setheading(90)
        self.reset()


    def reset(self):
        self.setposition(STARTING_POSITION)


    def move_up(self):
        y_pos = self.ycor()
        self.sety(y_pos + MOVE_DISTANCE)


    def move_down(self):
        y_pos = self.ycor()
        self.sety(y_pos - MOVE_DISTANCE)
