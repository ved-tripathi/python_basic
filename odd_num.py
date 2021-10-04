#program to classify odd and even
a=int(input("enter a natural number:"))
if a%2==0:
    print("you entered an even number")
elif a%2==1:
    print("you entred a odd num")
else:
    print("you overruled the condition") 
b=str(input("if you want to exit, enter 'x' or enter 'yes'"))
while b=='yes':
    a=int(input("enter a natural number:"))
    if a%2==0:
        print("you entered an even number")
        print("***if you want to exit, press ctrl+c***")
    elif a%2==1:
        print("you entred a odd num")
        print("***if you want to exit, press ctrl+c***")
    else:
        print("you overruled the condition")
        print("***if you want to exit, press ctrl+c***")
else:
    print("you may exit the calculator")
    print("thank you")

