#tricked you
print("instrucions: \n 1)this program may need a calculator or if you are capable enough to calculate, it's okay \n 2)whenever we will ask 'done?', enter 'd'or if you may want to exit, press 'x' \n 3)you will be told to choose a number and the program also will be choosing a number ")
print("so, let's get started, choose a number between 1 and 10 and don't mention it")
a=str(input("done?:"))
if a=='d':
    print("multiply the number by 2")
    b=str(input("done?:"))
    if b=='d':
        print("add 2 to your product hence got")
        print("I too chose a number with you which is '5':")
        c=str(input("done?:"))
        if c=='d':
            print("multiply your sum to 5")
            d=str(input("done?:"))
            if d=='d':
                print("subtract the number I chose in the begining from your product")
                e=str(input("done?:"))
                if e=='d':
                    f=str(input("enter the number hence got:"))
                    l=list(f)
                    print("the number in the ones place is the number that I chose ;)")
                    print("The number you chose is in the tens place ;D that is",l[0])
                    g=str(input("if you want to do it one more time, enter  'continue' or enter 'exit'"))
                    while g=='continue':
                        print("so, let's get started, choose a number between 1 and 10 and don't mention it")
                        a=str(input("done?:"))
                        if a=='d':
                            print("multiply the number by 2")
                            b=str(input("done?:"))
                            if b=='d':
                                print("add 2 to your product hence got")
                                print("this time I will choose, '6':")
                                c=str(input("done?:"))
                                if c=='d':
                                    print("multiply your sum to 5")
                                    d=str(input("done?:"))
                                    if d=='d':
                                        print("subtract the number I chose in the begining from your product")
                                        e=str(input("done?:"))
                                        if e=='d':
                                            f=str(input("enter the number hence got:"))
                                            l=list(f)
                                            print("the number in the ones place is the number that I chose ;)")
                                            print("The number you chose is in the tens place ;D that is",l[0])
                                            g=str(input("if you want to do it one more time, enter  'continue' or enter 'exit'"))
                                        else:
                                            print("thank you")
                                    else:
                                        print("thank you")
                                else:
                                    print("thank you")
                            else:
                                print("thank you")
                        else:
                            print("thank you")        
                    else:
                        print("thank you")
                else:
                    print("thank you")
            else:
                print("thank you")
        else:
            print("thank you")
    else:
        print("thank you")
else:
    print("thank you")
    


