from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.create_car()
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        new_car = Turtle("square")
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        random_color = choice(COLORS)
        new_car.color(random_color)
        new_car.penup()
        random_y = randint(-250, 250)
        new_car.goto(x=300, y=random_y)
        self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
