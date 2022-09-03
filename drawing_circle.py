'''import turtle

turtle.speed(0)
turtle.color('red','green')
turtle.begin_fill()
while True:
    turtle.forward(300)
    turtle.left(250)
    if abs(turtle.pos())<1:
        break
turtle.end()
turtle.done()

from turtle import *

bgcolor('black')
speed(0)
hideturtle()
for i in range(120):
    color('red')
    circle(i)
    color('orange')
    circle(i * 0.8)
    right(3)
    forward(3)
done'''

from sketchpy import library as lib

obj = lib.rdj()
obj.draw()