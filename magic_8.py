import turtle as tr
import colorsys as cs
tr.tracer(2)
tr.bgcolor("black")
tr.pensize(2)
n=100
h=0
for i in range(1000):
    for i in range(4):
        c=cs.hsv_to_rgb(h,1,1)
        h+=1/n
        tr.color(c)
        tr.circle(49+i*5,90)
        tr.forward(100)
        tr.left(90)
    tr.right(10)

tr.done()