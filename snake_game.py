import turtle
import time
import random

tail_list = []  # creating list for assign the tail length

# creating game window
window = turtle.Screen()
window.title("snake game")
window.bgcolor("black")
window.setup(width=600, height=600)
window.tracer(0)

# creating snake head
head = turtle.Turtle()
head.shape("square")
head.color("green")
head.speed(0)
head.penup()
head.goto(0, 0)
head.direction = "stop"

# creating food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.speed(0)
food.penup()
food.goto(0, 150)
food.shapesize(0.5, 0.5)

# creating score board

'''
score = turtle.Turtle
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("score : 0",align="center",font=("courier",20,"normal"))
'''


# function for calling the area to move
def move_up():
    if head.direction != "down":
       head.direction = "up"


def move_down():
    if head.direction != "up":
        head.direction = "down"

def move_left():
    if head.direction != "right":
        head.direction = "left"


def move_right():
    if head.direction != "left":
        head.direction = "right"


# function for moving the head
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# for listen which key is pressed
window.listen()
window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")
window.onkeypress(move_right, "d")
window.onkeypress(move_left, "a")

# main loop for run the functions
while True:
    window.update()

    # for end game when snake touch the border
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        time.sleep(0.5)
        turtle.color("white")
        turtle.write("GAME OVER", font=("courier", 25, "normal"), align="center")
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        turtle.clear()

        for list in tail_list:
            list.goto(1000, 1000)
        tail_list.clear()

    if head.distance(food) < 15:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # creating tail for snake when the food was eaten
        tail = turtle.Turtle()
        tail.shape("square")
        tail.color("green")
        tail.speed(0)
        tail.penup()
        tail.goto(5, 5)
        tail_list.append(tail)

    # loop for increase the length of the snake
    for index in range(len(tail_list) - 1, 0, -1):
        x = tail_list[index - 1].xcor()
        y = tail_list[index - 1].ycor()
        tail_list[index].goto(x, y)

    if len(tail_list) > 0:
        x = head.xcor()
        y = head.ycor()
        tail_list[0].goto(x, y)

    move()  # calling the main function

    # for end the game when snake touch in body
    for list in tail_list:
        if list.distance(head) < 20:
            time.sleep(0.5)
            turtle.write("GAME OVER", font=("courier", 25, "normal"), align="center")
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            turtle.clear()

            for list in tail_list:
                list.goto(1000, 1000)
            tail_list.clear()

    time.sleep(0.1)  # delaying the update of the window

window.mainloop()
