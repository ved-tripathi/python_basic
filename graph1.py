import turtle
import pdb
t=turtle.Turtle()
t.hideturtle()
t.speed(120)
t.fd(650)
t.home()
t.bk(660)
t.home()
t.rt(90)
t.fd(350)
t.bk(700)
t.goto(0,0)
for i in range(34):
    t.pencolor("grey")
    t.penup()
    t.bk(10)
    t.pendown()
    t.rt(90)
    t.fd(5)
    t.bk(10)
    t.fd(5)
    t.lt(90)
    t.penup()
t.goto(0,0)
for i in range(34):
    t.fd(10)
    t.rt(90)
    t.pendown()
    t.fd(5)
    t.bk(10)
    t.fd(5)
    t.lt(90)
    t.penup()
    
t.goto(0,0)
t.rt(90)

t.fd(10)
t.rt(90)
t.pendown()
t.fd(5)
t.bk(10)
t.fd(5)
t.lt(90)
t.penup()
#


for i in range(65):
    t.fd(10)
    t.rt(90)
    t.pendown()
    t.bk(5)
    t.fd(10)
    t.bk(5)
    t.lt(90)
    t.penup()    
t.goto(0,0)
t.rt(180)
#
for i in range(65):
    t.fd(10)
    t.lt(90)
    t.pendown()
    t.fd(5)
    t.bk(10)
    t.fd(5)
    t.rt(90)
    t.penup()
t.penup()
t.goto(100,100)
t.color("red")
t.write("scale: 1unit = 10 turtle units", font=("Bradley Hand ITC", 18, "bold"))


    
