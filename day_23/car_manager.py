from turtle import Turtle
import random as r

HEIGHT = int(600)
WIDTH = int(16 * HEIGHT / 9)
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 11
MOVE_INCREMENT = 7


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = r.randint(1, 7)
        if random_chance == 1:
            new_car = Turtle('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.pu()
            new_car.color(r.choice(COLORS))
            random_y = r.randint(int(-((HEIGHT/2)-50)), int((HEIGHT/2)-50))
            new_car.goto(WIDTH/2, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
        for car in self.all_cars:
            car.backward(self.car_speed)
