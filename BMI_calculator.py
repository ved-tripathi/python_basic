# BMI Calculator
print("this program will tell you your Body Mass Index (BMI) and your health criteria")
m=float(input("enter your current weight:"))
he=float(input("enter your current height:"))
cm=str(input("if your height was in centimeters enter 'cm' or if the height you entered, was in meters, enter 'm' :"))
#block 1
if cm=='m':
    h=he*he
    BMI=m/h
    print("your BMI is",BMI)           
elif cm=='cm':
    height=he/100
    h=height*height
    BMI=m/h
    print("your BMI is",BMI)
else:
    print("you overruled the cndition:")
#block 1 end    
# block 2
if BMI<=18 :
    print("you are under weight")
elif BMI<=24 :
    print("you are healthy")
elif BMI<=29 and BMI>24 :
    print("you are ovrweight")
elif BMI<=39 and BMI>29 :
    print("you are obese")
elif BMI>=40 :
    print("you are extremely obese. Need to work hard")
# block 2 end    

    
    
