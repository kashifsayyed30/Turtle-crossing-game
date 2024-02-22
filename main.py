import time
from turtle import Screen
from car_manager import CarManager
from player import Player
from score import Score

screen = Screen()
screen.setup(600, 600)
screen.title("Turtle Crossing")
screen.bgcolor("light blue")
screen.tracer(0)

player = Player()
car_manager = CarManager()
score = Score()
game_on = True

screen.listen()
screen.onkey(player.move_up, "Up")

while game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # detect car with collision
    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            game_on = False
            score.game_over_text()

    #detect successful crossing
    if player.at_finish():
        player.go_at_start()
        car_manager.level_up()
        score.increment_level()


screen.exitonclick()
