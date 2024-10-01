import turtle
import random
import math


def stop():
    turtle.bye()


def prepare_turtle_canvas():
    turtle.setup(1024, 768)
    turtle.bgcolor(0.2, 0.2, 0.2)
    turtle.penup()
    turtle.hideturtle()
    turtle.shape('arrow')
    turtle.shapesize(2)
    turtle.pensize(5)
    turtle.color(1, 0, 0)
    turtle.speed(100)
    turtle.goto(-500, 0)
    turtle.pendown()
    turtle.goto(480, 0)
    turtle.stamp()
    turtle.penup()
    turtle.goto(0, -360)
    turtle.pendown()
    turtle.goto(0, 360)
    turtle.setheading(90)
    turtle.stamp()
    turtle.penup()
    turtle.home()

    turtle.shape('circle')
    turtle.pensize(1)
    turtle.color(0, 0, 0)
    turtle.speed(50)

    turtle.onkey(stop, 'Escape')
    turtle.listen()


def draw_big_point(p):
    turtle.goto(p)
    turtle.color(0.8, 0.9, 0)
    turtle.dot(15)
    turtle.write('     '+str(p))


def draw_point(p):
    turtle.goto(p)
    turtle.dot(5, random.random(), random.random(), random.random())


def draw_line_mak_coding(p1, p2):
    draw_big_point(p1)
    draw_big_point(p2)

    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]

    # 기울기와 절편값
    a = (y2 - y1)/(x2 - x1)
    b = y1 - a * x1     # y2 - a * x2

    for x in range (x1, x2, 10):
        y = a * x + b
        draw_point((x, y))

    draw_point(p2) # 마지막 포인트 강제 출력

def draw_line(p1, p2):
    draw_big_point(p1)
    draw_big_point(p2)
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]

    for i in range(0, 100):
        t = i / 100

        x = (1 - t) * x1 + t * x2 # x1:x2 = 1-t:t
        y = (1 - t) * y1 + t * y2 # y1:y2 = 1-t:t

        draw_point((x, y))

    draw_point(p2)

def draw_apple_shape():

    for i in range(0, 100 + 1):
        t = i / 100 * math.pi * 2
        a = 400 * (0.5 + 0.4*math.cos(t)+0.1*math.sin(2*t))/(1+0.7*math.cos(t))
        x = a * math.cos(t)
        y = a * math.sin(t)

        draw_point((x, y))

prepare_turtle_canvas()

p1 = (-100, -100)
p2 = (300, 150)

draw_apple_shape()

draw_line(p1, p2) # 두개의 점, 튜플을 활용

draw_line ((-100, -100), (-100, 150))

turtle.done()