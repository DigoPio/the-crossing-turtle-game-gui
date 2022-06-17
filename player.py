from turtle import Turtle

UP = 90
DOWN = 270
STARTING_POSITION = (0, -280)
FINISH_LINE = 0, 300
MOVE_DISTANCE = 10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('green')
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(UP)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_down(self):
        self.backward(MOVE_DISTANCE)








