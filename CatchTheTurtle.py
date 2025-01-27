import turtle
import random

screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("Catch the Turtle")
top_height = screen.window_height() / 2

turtle_instance = turtle.Turtle()
def set_turtle_instance():
    global turtle_instance
    turtle_instance.color("dark green")
    turtle_instance.shape("turtle")
    turtle_instance.shapesize(stretch_wid=2, stretch_len=2)
    turtle_instance.penup()
    turtle_instance.speed(0)

def set_timer_turtle():
    global timer, timer_turtle
    timer_turtle = turtle.Turtle()
    timer_turtle.hideturtle()
    timer_turtle.penup()
    timer_turtle.goto(0, top_height * 0.7)
    timer = 20
def update_timer():
    timer_turtle.clear()
    timer_turtle.write(f"Time: {int(timer)}", align="center", font=("Arial", 18, "bold"))

def set_score_turtle():
    global score, score_turtle
    score_turtle = turtle.Turtle()
    score_turtle.color("blue")
    score_turtle.hideturtle()
    score_turtle.penup()
    score_turtle.goto(0, top_height * 0.8)
    score = 0
def update_score():
    score_turtle.clear()
    score_turtle.write(f"Score: {int(score)}", align="center", font=("Arial", 18, "bold"))

def move_turtle():
    global timer, x, y
    width = screen.window_width() // 3
    height = screen.window_height() // 3
    if timer > 0:
        x = random.randint(-width, width)
        y = random.randint(-height, height)
        turtle_instance.goto(x, y)

        timer -= 0.6
        update_timer()
        screen.ontimer(move_turtle, 600)
    else:
        timer_turtle.clear()
        timer_turtle.goto(0, 200)
        timer_turtle.write("Game Over!", align="center", font=("Arial", 24, "bold"))
        turtle_instance.hideturtle()

def click(a, b):
    global score
    score += 1
    update_score()

def start_game():
    turtle.tracer(0)
    set_turtle_instance()
    set_score_turtle()
    set_timer_turtle()
    turtle.tracer(1)
    update_timer()
    update_score()
    move_turtle()
    turtle_instance.onclick(click, 1)

start_game()
turtle.mainloop()