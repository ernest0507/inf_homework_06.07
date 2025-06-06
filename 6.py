from turtle import *

tracer(0)
screensize(1500, 1500)
k = 15
lt(90)
down()


for _ in range(4):
    fd(19 * k)
    rt(90)
    fd(30 * k)
    rt(90)

up()

fd(2 * k)
rt(90)
fd(8 * k)
lt(90)

down()

for _ in range(4):
    fd(93 * k)
    rt(90)
    fd(97 * k)
    rt(90)

up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * k, y * k)
        dot(3, 'red')

exitonclick()
