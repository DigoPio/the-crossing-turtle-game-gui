from turtle import Turtle
import random

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENTS = 5
colors = ['blue', 'orange', 'red', 'black']



class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.difficulty = 1
        self.chance = 6
        self.hideturtle()
        self.penup()

    def create_car(self):
        cars_chance = random.randint(1, self.chance)
        if cars_chance == 1:
            new_car = Turtle('square')
            new_car.shapesize(1, 2)
            new_car.color(random.choice(colors))
            new_car.penup()
            new_car.goto(300, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE + (MOVE_INCREMENTS * self.difficulty))


















