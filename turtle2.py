
from turtle import *
speed(1000)
color('black','red')
k = 20
tracer(3)
begin_fill()
for i in range(2):
    forward(8 * k)
    right(90)
    forward(18 * k)
    right(90)
pu()
forward(4 * k)
right(90)
forward(10*k)
left(90)
pd()
for i in range(2):
    forward(17*k)
    right(90)
    forward(7 * k )
    right(90)
end_fill()
pu()
#for x in range(-30, 30):
  #for y in range(-30, 30):
    #goto(x * k, y * k)
    #dot(5, "red")
    #dot(2, "white")

canvas = getcanvas()

counter = 0
for x in range(-120*k, 100*k, k):
    for y in range(-120*k, 120*k, k):
        item = canvas.find_overlapping(x, y, x, y)
        if len(item) == 1 and (item[0] == 5 or item[0] ==4):
            counter +=1
print(counter)
mainloop()