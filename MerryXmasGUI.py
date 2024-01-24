# Libraries to use
import math, time, turtle
from turtlealphabets import main_app
from turtle import *

# Functions to draw the heart
def heart_a(x):
    return 15 * math.sin(x) ** 3

def heart_b(x):
    return 12 * math.cos(x) - 5 * math.cos(2 * x) - 2 * math.cos(3 * x) - math.cos(4 * x)


# Drawing the heart
t = turtle.Turtle()
turtle.title('Merry Christmas')
t.hideturtle()
t.speed(0)
bgcolor('black')
t.pensize(6)

for i in range(700):
    if i % 100 == 0:
        print(f'i - {i}')
    t.goto(heart_a(i) * 17, heart_b(i) * 17)
    for j in range(5):
        t.color('red')
    t.goto(0, 0)

t.pendown()
# displaying Merry Christmas on the screen
t.color('white')
t.write('Merry Christmas',align='center', font=('Arial', 50, 'italic'))
time.sleep(2)
t.clear()

# Displaying my name
# You can change it to urs
main_app(t,'Aycodez')
done()


