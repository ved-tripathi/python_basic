n=int(input("enter the number of terms you would like to see in fibonacci series:"))
print("you will see",n," of terms in fibonacci series")
fibo = [0,1]
for i in range (n):
    nacci=fibo[-1]
    bona=fibo[-2]
    fibo.append(bona+nacci)
    print(fibo)
    
print(fibo)
