
from turtle import *
speed(1000)
color('black','red')
k = 20
tracer(3)
begin_fill()
up()
fd(100)
rt(90)
fd(100)
rt(45)
down()
for i in range(15):
    fd(20)
    rt(90)
    fd(30)
    rt(90)
canvas = getcanvas()

counter = 0
for x in range(-120*k, 100*k, k):
    for y in range(-120*k, 120*k, k):
        item = canvas.find_overlapping(x, y, x, y)
        if len(item) == 1 and (item[0] == 5 or item[0] ==4):
            counter +=1
print(counter)
mainloop()