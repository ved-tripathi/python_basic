#program to make a calculator:
a=float(input("enter your first number :"))
print("your first number is:",a)
b=float(input("enter your second number:"))
print("your second number is:",b)
c=int(input("enter (1) to choose +,(2) to choose - , (3) to choose * and (4) to choose /:"))
if c==1:
    sum=a+b
    print("sum is:",sum)
elif c==2:
    sub=a-b
    print("difference is:",sub)
elif c==3:
    pro=a*b
    print("product is:",pro)
elif c==4 :
    div=a/b
    print("division is:",div)
else:
    print("you overruled the condition!!!")    
d=str(input("press 'yes' if you want to continue and 'no' if you want to exit"))
if d== 'yes' :
    a=float(input("enter your first number :"))
    print("your first number is:",a)
    b=float(input("enter your second number:"))
    print("your second number is:",b)
    c=int(input("enter (1) to choose +,(2) to choose - , (3) to choose * and (4) to choose /:"))
    if c==1:
        sum=a+b
        print("sum is:",sum)
    elif c==2:
        sub=a-b
        print("difference is:",sub)
    elif c==3:
        pro=a*b
        print("product is:",pro)
    elif c==4 :
        div=a/b
        print("division is:",div)
    else:
        print("you ovveruled the condition")
else:
    print("you may exit the calculator")
    print("**thank you** :) ")

        


        




    
    
    

    



      
