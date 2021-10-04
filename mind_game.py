print("this program gusses about your thinking")
print("the guesses may be wrong in the program")
print("you can play this game only once")
a=str(input("press 's' to start the mind game:"))


if a=='s':
    choose=str(input("choose a number between 1 and 10 and don't metion the number.   press c to get on the next instruction:"))
    if choose=='c':
        b=str(input("multiply the number with 2.  press c to get on the next instruction:"))
        if b=='c':
            c=str(input(" add 8 to the product .press c to get on the next instruction:"))
            if c=='c':
                d=str(input("divide the sum by 2 .press c to get on the next instruction:"))
                if d=='c':
                    e=str(input(" subtract the no. you chose from the number you hence got .press c to get on the next instruction:"))
                    print (''' A=1 B=2 C=3 D=4 ..........Z=26''')
                    print("if the final number you got is 1, you remember A if 2 was the final number, you remember B")
                    f=str(input("now,think of a country starting with the letter you have in your mind.press c to get on the next instruction:"))
                    if f=='c':
                        print("imagine a name of an animal starting with the second letter of the name 'if the name is france, you'll think a name of an animal from 'r'")
                        g=str(input("press c to get on the next instruction:"))
                        if g=='c':
                            print("now I am going to read your mind")
                            print(" the country you have in your mind is denmark")
                            print("the animal in your mind in an elephant")
            
                            
