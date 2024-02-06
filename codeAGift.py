import flet as ft
import turtle
from datetime import datetime


# Function to set up turtle environment
def setup():
    turtle.setup(width=800, height=600)
    turtle.speed(0)
    turtle.hideturtle()
    turtle.penup()
    turtle.bgcolor("pink")

# Function to draw a heart shape
def draw_heart(x, y, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("red")
    turtle.begin_fill()
    turtle.left(140)
    for _ in range(200):
        turtle.right(1)
        turtle.forward(2 * size)
    turtle.left(120)
    for _ in range(200):
        turtle.right(1)
        turtle.forward(2 * size)
    turtle.forward(224)
    turtle.end_fill()

# Function to draw a rose
def draw_rose(x, y, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("green")
    for _ in range(6):
        draw_petal(size)
        turtle.left(60)
    turtle.left(90)
    turtle.forward(200 * size)

# Function to draw a petal
def draw_petal(size):
    for _ in range(2):
        turtle.circle(40 * size, 60)
        turtle.left(120)

# Function to display proposal message
def display_message(message):
    turtle.penup()
    turtle.goto(0, -250)
    turtle.pendown()
    turtle.color("purple")
    turtle.write(message, align="center", font=("Arial", 20, "bold"))

# Main function
def wish():
    proposals = {
        "Rose Day": "Will you accept this rose and be my Valentine?",
        "Propose Day": "I have a question for you: Will you be my Valentine?",
        "Chocolate Day": "Like chocolates, you make my life sweeter. Will you be mine?",
        "Teddy Day": "Sending you a teddy bear hug! Will you be my cuddle buddy?",
        "Promise Day": "On this Promise Day, I promise to cherish and love you forever. Will you be mine?",
        "Hug Day": "Sending warm hugs your way! Will you be my Valentine?",
        "Kiss Day": "Can I steal a kiss from you? Will you be my Valentine?",
    }

    setup()
    days = {
    "07-02": "Rose Day",
    "08-02": "Propose Day",
    "09-02": "Chocolate Day",
    "10-02": "Teddy Day",
    "11-02": "Promise Day",
    "12-02": "Hug Day",
    "13-02": "Kiss Day",
    "14-02": "Valentine's Day"
    }

    today = datetime.now().strftime("%d-%m")
    day = days[today]
    print(day)
    message =  proposals[day]
    turtle.reset()
    turtle.title(day)
    turtle.speed(0)
    if day == "Rose Day":
        draw_rose(0, 100, 0.5)
    else:
        draw_heart(0, 100, 2)
    display_message(message)
    turtle.done()


def main(page):
    page.window_width=200
    page.window_height=200
    page.add(ft.ElevatedButton("Wish Me", bgcolor="pink", color="white", on_click=lambda e: wish()))


ft.app(target=main)