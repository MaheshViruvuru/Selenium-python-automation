import turtle

colors = ["red", "Purple", "blue", "orange", "green"]

t = turtle
turtle.bgcolor('black')
for i in range(360):
    t.pencolor(colors[i % 5])
    t.width(i/100+0.5)
    t.backward(i)
    t.right(71)



