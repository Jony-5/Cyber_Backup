from turtle import *
speed(1)
color('red', 'yellow')
begin_fill()
while True:
    forward(250)
    left(150)
    if abs(pos()) < 1:
        break
end_fill()
done()
