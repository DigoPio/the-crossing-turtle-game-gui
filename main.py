import time
from turtle import Screen
from player import Player
from cars import Cars
from score import Score


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('gray')
screen.title("DigoPio's Turtle Cross")
screen.tracer(0)



score = Score()
player = Player()
car = Cars()


screen.listen()
screen.onkey(player.go_up, 'Up')
screen.onkey(player.go_down, 'Down')


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    score.write_score()
    score.write_level()
    car.create_car()
    car.move_cars()
    for cars in car.all_cars:
        if player.distance(cars) < 20:
            score.write_game_over()
            game_is_on = False
    if player.ycor() == 300:
        player.goto(0, -280)
        score.score += 1
        score.clear()
    if score.score == 5:
        car.difficulty += 1
        car.chance -= 1
        score.score = 0
        score.level += 1
    elif score.level == 10:
        score.write_you_won()
        game_is_on = False
    

screen.exitonclick()
