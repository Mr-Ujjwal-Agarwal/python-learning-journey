import turtle as t
import random 

screen = t.Screen()
screen.title("WELCOME TO RETRO GAMES")
screen.bgcolor("lightblue")
screen.setup(width = 600 , height = 600)


score_display = t.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(-250 , 250)
score_display.write("Score : 0 ", font = ("Arial",16,"bold"))


player = t.Turtle()
player.shape("square")
player.color("blue")
player.shapesize(2)
player.penup()
player.goto(0,-250)


food = t.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(random.randint(-250,250),250)


def left():
    x = player.xcor()
    x = x - 30

    if x < -260:
        x = -260

    player.setx(x)


def right():
    x = player.xcor()
    x = x + 30

    if x > 260:
        x = 260

    player.setx(x)


screen.listen()
screen.onkeypress(left , "Left")
screen.onkeypress(right , "Right")
score = 0

while True :
    y = food.ycor()
    y -= 3
    food.sety(y)

    if player.distance(food) < 40:
        score = score + 1
        score_display.clear()
        score_display.write(f"score : {score}", font=("Arial",10 ,"bold"))
        food.goto(random.randint(-250,250),250)

    if food.ycor() < -300:
        food.goto(random.randint(-250,250),250)

screen.mainloop()
