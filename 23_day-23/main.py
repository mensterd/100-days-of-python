import time
import init
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=init.SCREEN_WIDTH, height=init.SCREEN_HEIGHT)
screen.title("Turtle Crossing")
# Hide animation
screen.tracer(0)

screen.listen()

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

game_is_on = True

def end_game():
    global game_is_on
    game_is_on = False



# Exits loop with 'Q' key
screen.onkey(end_game, key="q")
screen.onkey(player.move_up, key="Up")
screen.onkey(player.move_down, key="Down")



while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            game_is_on = False
            scoreboard.game_over()

    # Detect safe crossing
    if player.ycor() >= (init.SCREEN_HEIGHT / 2):
        player.reset()
        car_manager.level_up()
        scoreboard.raise_score()



screen.exitonclick()