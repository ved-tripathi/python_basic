print("In python, hexadecimal numbers start from '#' or '0x' so, to get the hexadecimal number, remove the '0x' or '#'")
def hex_sum ():
    inp = str(input("enter the first hexadecimal no. (hex) :"))
    inp2 = str(input("enter the second hex:"))
    num2 = (int(inp2, base = 16))
    num1 = (int(inp, base = 16))
    sum0 = num1 + num2
    hex_final = (hex(sum0))
    print(hex_final)
hex_sum()




'''>>> import turtle
>>> t = turtle.Turtle()
>>> inp = str(input("enter the first hexadecimal no. (hex) :"))
enter the first hexadecimal no. (hex) :6
>>> inp = str(input("enter the first hexadecimal no. (hex) :"))
enter the first hexadecimal no. (hex) :646d7e
>>> inp = str(inp)
>>> inp = ("#" + inp)
>>> print(inp)
#646d7e


for i in range(400):
	r = ("%s" %i)
	r = (int(i, base = 16))
	t.color(inp)
	t.circle(i)
	inp = (int(inp, base = 16))
	inp = (sum(inp,r))
	inp = (str(inp))



for i in range(400):

	r = (num1+i)
	inp = (hex(r))

	t.color(hex(num1))
	t.circle(i)
	inp = (int(inp, base = 16))
	inp = (sum(inp,r))
	inp = (str(inp))



for i in range (400):
	inp2 = str(i)
	num1 = (int(inp ,base = 16))
	num2 = (int(inp2 ,base= 16))
	sum0 = num1 + num2
	hex_final = (hex(sum0))
	hex_final2 = str(hex_final)
	hex_final3 = hex_final2[2:]
	hex_final4 = ("#" + hex_final3)
	t.color(hex_final4)
	t.circle(i)



def light():
	inp = str(input("enter hex:"))
	t.speed(10)
	t.pensize(2)
	for i in range(1,400):
		inp2 = str(i)
		num1 = int(inp, base=16)
		num2 = int(inp2,  base = 16)
		sum0 = num1 + num2
		hex_final = hex(sum0)
		hex_final2 = str(hex_final)
		hex_final3 = hex_final2[2:]
		hex_final4 = ("#" + hex_final3)
		t.penup()
		t.goto(0,(-i+2))
		t.pendown()
		t.color(hex_final4)
		t.circle(i)'''
