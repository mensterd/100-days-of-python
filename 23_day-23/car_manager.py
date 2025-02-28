from turtle import Turtle
import random
import init


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = init.CAR_STARTING_SPEED
        self.hideturtle()
        self.penup()


    def create_car(self):
        # Takes care of not to much cars on the road. Only a 1 in b change that there will be a car created
        random_int = random.randint(a=1,b=init.CAR_RANDOMIZATION)
        if random_int == 1:
            new_car = Turtle("square")
            # Stretches turtle to widith 2x20=40 and length 1x20=20 px.
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(init.CAR_COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(x=300, y=random_y)
            self.all_cars.append(new_car)


    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)


    def level_up(self):
        self.car_speed += init.CAR_SPEED_INCREMENT


