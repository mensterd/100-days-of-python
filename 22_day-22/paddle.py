from turtle import Turtle
import init

class Paddle(Turtle):
    def __init__(self, start_position, color=init.PADDLE_DEF_COLOR):
        super().__init__("square")
        self.x_pos = start_position[0]
        self.y_pos = start_position[1]
        self.color(color)
        self.penup()
        self.speed("fastest")
        self.setposition(x=self.x_pos, y=self.y_pos)
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.paddle_speed = 30



    def move_up(self):
        new_y = self.ycor() + self.paddle_speed
        self.goto(x=self.x_pos, y=new_y)
        print("UP")

    def move_down(self):
        new_y = self.ycor() - self.paddle_speed
        self.goto(x=self.x_pos, y=new_y)
        print("Down")














