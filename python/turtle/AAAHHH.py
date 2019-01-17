import turtle
import math
import random
wn = turtle.Screen()
wn.bgcolor('black')
Albert = turtle.Turtle()
Albert.speed(0)
Albert.color('green')
rotate=int(360)
def drawCircles(t,size):
    for i in range(10):
        t.circle(size)
        size=size-4
def drawSpecial(t,size,repeat):
  for i in range (repeat):
    drawCircles(t,size)
    t.right(360/repeat)
drawSpecial(Albert,100,20)
Steve = turtle.Turtle()
Steve.speed(0)
Steve.color('blue')
rotate=int(90)
def drawCircles(t,size):
    for i in range(5):
        t.circle(size)
        size=size-10
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawSpecial(Steve,100,30)
barry = turtle.Turtle()
barry.speed(0)
barry.color('red')
rotate=int(175)
def drawcircles(t,size):
	for i in range(16):
		t.circle(size)
		size=size-20
def drawspecial(t,size,repeat):
	for i in range (repeat):
		drawCircles(t,size)
		t.right(360/repeat)
drawspecial(barry,100,40)
holdit=input()
