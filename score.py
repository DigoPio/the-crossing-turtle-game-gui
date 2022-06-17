from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color('blue')
        self.speed('fastest')
        self.hideturtle()
        self.setheading(90)
        self.penup()
        self.score = 0
        self.level = 1

    def write_score(self):
        self.goto(0, 265)
        self.pendown()
        self.write(f"Score:{self.score}", False, align="center", font=('Arial', 20, 'normal'))
        self.penup()

    def write_level(self):
        self.goto(-200, 250)
        self.pendown()
        self.write(f"Level:{self.level}", False, align="center", font=('Arial', 20, 'normal'))
        self.penup()

    def write_game_over(self):
        self.goto(0, 0)
        self.pendown()
        self.write(f"GAME OVER", False, align="center", font=('Arial', 20, 'normal'))
        self.penup()

    def write_you_won(self):
        self.goto(0, 0)
        self.pendown()
        self.write(f"CONGRATULATIONS! YOU WON THE GAME!", False, align="center", font=('Arial', 20, 'normal'))
        self.penup()