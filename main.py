import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard= Scoreboard()

screen.listen()
screen.onkey(player.goUp, "Up")
screen.onkey(player.goUp, "w")
screen.onkey(player.goDown, "Down")
screen.onkey(player.goDown, "s")



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.createCar()
    car_manager.moveCars()

    for car in car_manager.getAllCare():
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.gameOver()

    if player.isAtFinishLine():
        player.goToStart()
        car_manager.levelUp()
        scoreboard.increaseLevel()

screen.exitonclick()