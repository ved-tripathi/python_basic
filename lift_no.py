# import graph1
import turtle


screen =turtle.Screen()
t = turtle.Turtle()
# import graph2
t.hideturtle()
t.penup()
t.lt(90)
t.fd(350)
t.bk(10)
t.rt(90)
t.fd(70)
t.rt(90)
t.pensize(3)
t.pendown()


def floors():
    floor = [11,10,9,8,7,6,5,4,3,2,1,"G"]
    for i in floor:
        t.fd(55.83)
        t.penup()
        t.rt(90)
        t.fd(12)
        t.pendown()
        t.write(i, align='left')
        t.rt(180)
        t.fd(12)
        t.rt(90)


def lift():
    t.penup()
    #t.goto(80.00,340.87)
    t.pendown()
    t.color("blue", "orange")
    t.begin_fill()
    for i in range(4):
        t.fd(50)
        t.lt(90)
    t.end_fillscreen = turtle.Screen()
screen.setup(600, 600)
#screen.bgcolor('green')
screen.tracer(2)
move = turtle.Turtle() 
move.color('orange')
move.speed(0)
move.width(2)
move.hideturtle()
move.penup()
move.goto(-250, 0)
move.pendown()

floors()
t.penup()
t.goto(80.00,340.87)
t.pendown()
#i=0
#def call(x):
    
for i in range (207):  # number of loops depend on line number 70 :
#    i = i+1           #  for example:                                    
    move.clear()       #__________*****Case I*****_________________________________________|                       
    lift()             #if turtle heads by (0.5 pixels),      |no. of pixels,              |     
    screen.update()    #the number of loops should be (1240)  |is directly proportional to,| 
                       #                                      |speed of the lift           |      
    t.speed(1)         #__________*****Case II****____________|____________________________|
    t.fd(3)            #if pixels heads by (3 pixels), the (loop count = 206.6667)         |
                       # 0.5 is the lowest count tested
#    print(i)          # formula: let 0.5(a) = required no. of pixels; let's call it "n"
                       # 1240/a = number of loops
                       
                       #NOTE: if 1240/a is a decimal number, take it's approx.
                       #                             ...As done in CASE II





