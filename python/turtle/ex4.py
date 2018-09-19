#https://www.geeksforgeeks.org/turtle-programming-python/
import turtle  #Inside_Out
wn = turtle.Screen()
wn.bgcolor("#00ff00")
cr = turtle.Turtle()
cr.color("blue")

def sqrfunc(size):
    for i in range(1):
        cr.fd(size)
        cr.right(160)
        size = size + 45

sqrfunc(41)
sqrfunc(78)
sqrfunc(64)
sqrfunc(56)
sqrfunc(47)
sqrfunc(37)
sqrfunc(27)
sqrfunc(12)
holdit = input();
