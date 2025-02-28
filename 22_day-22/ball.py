from turtle import Turtle
import init

class Ball(Turtle):
    def __init__(self, start_pos=(0,0)):
        super().__init__(init.BALL_SHAPE)
        self.color(init.BALL_COLOR)
        self.setposition(start_pos)
        self.penup()
        self.speed("normal")
        self.x_move = 10
        self.y_move = 10



    def move(self, direction):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.setposition(new_x, new_y)
        print(new_x, new_y)


    def bounce_x(self):
        self.x_move *= -1


    def bounce_y(self):
        self.y_move *= -1


    def reset_position(self):
        self.goto(0,0)