#program to find weather the no. is prime or not
num=int(input("enter a positive integer"))

for i in range(2,num):
    if (num % i) == 0:
        print(num,"is not a prime number")
        print(i,"*",num//i,"=",num)

print(num,"is a prime number")

        
    

   
            
    
