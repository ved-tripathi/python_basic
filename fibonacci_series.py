import turtle
t=turtle.Turtle()
n=int(input("enter the number of terms you would like to see in fibonacci series:"))
print("you will see",n,"number of terms in fibonacci series")
fibo = [0,1] 
for i in range (n):
    r = fibo[-1]
    r2 = fibo[-2]
    t.circle(r,180)
    fibo.append(r+r2)
    print(fibo)
'''for i in range (n):
#i=0
#for i in range(1,100):
#	t.circle(fibo,180)
#	fibo = fibo + fibo
#	print(fibo)
#while (fibo[-1]<610):
#    i=i+1
#    print(i)
    last_n=fibo[-1]
    sec_last_n=fibo[-2]
    fibo.append(bona+nacci)
#    print(fibo)
    t.circle(nacci,180)
#    fibo = fibo+fibo
#    print(fibo)
print(fibo)'''
