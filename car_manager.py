from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
  
    def __init__(self) -> None:
        self.all_care = []
        self.care_speed = STARTING_MOVE_DISTANCE

    def getAllCare(self):
        return self.all_care

    def createCar(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square") 
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_care.append(new_car)

    def moveCars(self):
        for car in self.all_care:
            car.backward(self.care_speed)

    def levelUp(self):
        self.care_speed += STARTING_MOVE_DISTANCE