#area and volume
a=str(input("if you want to find area, enter 'area' or if you want to find volume of any shape, enter 'volume' for exiting, press 'r':"))
pi=3.14
if a=='area':
    b=str(input("enter the name of shape:"))
    if b=='square':
        c=float(input("enter the length of the side:"))
        print("area=side*side")

        print(".:area=",c*c)
    elif b=='triangle':
        d=float(input("enter the length of base"))
        e=int(input("enter the length of height"))
        print("area=1/2*base*height")
        print(0.5*d*e)
    elif b=='circle':
        d=float(input("enter the length of radius"))
        print("Area of circle =π*radius^2")
        print(".: area=",pi*d*d)
    elif b=='rectangle':
        d=float(input("enter the length:"))
        e=float(input("enter the breadth"))
        print("area of rectangle=length*breadth")
        print("area =",d*e)
    elif b=='semi-circle':
        d=float(input("enter the radius:"))
        print("area=",pi*d*d*0.5)
    elif b=='hexagon':
        c=float(input("enter the side of the shape:"))
        print("area of hexagon= (3√3)side*side/2") 
        print("area=",3*1.7320508075688772935274463415058723669428052*c*c/2)    
    elif b=='cube':
        d=float(input("enter the length of side"))
        e=str(input("if you want to find total surface area, enter 'TSA' or if you want to find lateral surface area, enter 'CSA' "))
        if e=='TSA' or 'tsa':
            print("total surface area of cube=6(side)^2")
            print("toal surface area=",6*d*d)
        elif e=='CSA' or 'csa':
            print("lateral surface area of cube=4(side)^2")
            print("lateral surface area=",4*d*d)
        else:
            print("you overruled the condition")
    elif b=='cuboid':
        c=float(input("enter the mesurement of height(h):"))
        d=float(input("enter the measurement of breadth(b):"))
        f=float(input("enter the measurement of length(l):"))
        e=str(input("if you want to find total surface area, enter 'TSA' or if you want to find lateral surface area, enter 'CSA' "))
        if e=='TSA' or 'tsa':
            print("total surface area of cuboid=2(lb+bh+hl)")
            print("total surface area=",2*f*d+2*d*c+2*f*c)
        elif e=='CSA' or 'csa':
            print("lateral surface area of cuboid=2h(l+b)")
            print("lateral surface area=",2*h*l+2*h*b)
        else:
            print("you overruled the condition")
    elif b=='cone':
        c=float(input("enter the slant height:"))
        d=float(input("enter the height:"))
        f=float(input("enter the base radius:"))
        e=str(input("if you want to find total surface area, enter 'TSA' or if you want to find curved surface area, enter 'CSA' "))
        if e=='TSA' or 'tsa':
            print("total surface area of cone=πrl+πr^2")
            print("total surface area=",pi*c*f+pi*f*f)
        elif e=='CSA' or 'csa':
            print("curved surface area of cone=πrl")
            print("curved aurface area=",pi*f*c)
        else:
            print("you overruled the condition")
    elif b=='cylinder':
        c=float(input("enter the radius:"))
        d=float(input("enter the height:"))
        e=str(input("if you want to find total surface area, enter 'TSA' or if you want to find curved surface area, enter 'CSA' "))
        if e=='TSA' or 'tsa':
            print("total surface area of cylinder=2πr(r+h)")
            print("total surface area=",2*pi*c*c+2*pi*c*d)
        elif e=='CSA' or 'csa':
            print("curved surface area of cylinder=2πrh")
            print("curved surface area=",2*pi*c*d)
        else:
            print("you overruled the condition")
    elif b=='sphere':
        c=float(input("enter the radius:"))
        print("area of sphere=4πr^2")
        print("area=",4*pi*c*c)
    elif b=='hemisphere' or 'hemi-sphere':
        c=float(input("enter the radius:"))
        e=str(input("if you want to find total surface area, enter 'TSA' or if you want to find curved surface area, enter 'CSA' "))
        if e=='TSA' or 'tsa':
            print("total surface area of hemisphere=3πr^2")
            print("total surface area=",3*pi*c*c)
        elif e=='CSA' or 'csa':
            print("curved surface area of hemisphere=2πr^2")
            print("curved surface area=",2*pi*c*c)
        else:
            print("you overruld the condition")
    elif b=='frustum':
        c=float(input("enter the radius of the smaller circle(r):"))
        d=float(input("enter the radius of bigger circle(R):"))
        f=float(input("enter the slant height(l):"))
        e=str(input("if you want to find total surface area, enter 'TSA' or if you want to find curved surface area, enter 'CSA' "))
        if e=='TSA' or 'tsa':
            print("total surface area of frustum=πl(R+r)+π(R^2+r^2)")
            print("total surface area=",pi*f*d+pi*f*c+pi*d*d+pi*c*c)
        elif e=='CSA' or 'csa':
            print("curved surface area of frustum =πl(R+r)")
            print("curved surface area =",pi*f*d+pi*f*c)
        else:
            print("you overruled the condititon!!")
    else:
        print("you overruled the condition!!")
elif a=='volume':
    b=str(input("enter the name of shape:"))
    if b=='cube':
        c=float(input("enter the length of the side:"))
        print("volume=side^3")
        print("volume=",c*c*c)
    elif b=='cuboid':
        c=float(input("enter the mesurement of height(h):"))
        d=float(input("enter the measurement of breadth(b):"))
        e=float(input("enter the measurement of length(l):"))
        print("volume of cuboid=l*b*h")
        print("volume=",c*d*e)
    elif b=='cone':
        d=float(input("enter the height:"))
        e=float(input("enter the base radius:"))
        print("volume of cone = πr^2*h/3")
        print(pi*e*e*d/3)
    elif b=='cylinder':
        c=float(input("enter the radius:"))
        d=float(input("enter the height:"))
        print("volume of cylinder =πr^2h")
        print("volume=",pi*c*c*d)
    elif b=='sphere':
        c=float(input("enter the radius:"))
        print("volume of sphere = 4/3*πr^3")
        print("volume=",4/3*pi*c*c*c)
    elif b=='hemisphere':
        c=float(input("enter the radius:"))
        print("volume of sphere=2/3 πr^3")
        print("volume=",2/3*pi*c*c*c)
    elif b=='frustum':
        c=float(input("enter the radius of the smaller circle:"))
        d=float(input("enter the radius of the bigger circle:"))
        e=float(input("enter the height:"))
        print("volume of frustum=1/3*π*h(r^2+R^2+R*r")
        print("volume=",1/3*pi*e*c*c+1/3*pi*e*d*d+1/3*pi*e*d*c)
    else:
        print("you overruled the condition")
elif a=='r':
    print("good bye")
else:
    print("you overruled the condition!!!")
z=str(input("if you want to do it again enter 'again'"))    
while z=='again':
    a=str(input("if you want to find area, enter 'area' or if you want to find volume of any shape, enter 'volume' for exiting, press 'r':"))
    pi=3.14
    if a=='area':
        b=str(input("enter the name of shape:"))
        if b=='square':
            c=float(input("enter the length of the side:"))
            print("area=side*side")
            print(".:area=",c*c)
        elif b=='triangle':
            d=float(input("enter the length of base"))
            e=int(input("enter the length of height"))
            print("area=1/2*base*height")
            print(0.5*d*e)
        elif b=='circle':
            d=float(input("enter the length of radius"))
            print("Area of circle =π*radius^2")
            print(".: area=",pi*d*d)
        elif b=='rectangle':
            d=float(input("enter the length:"))
            e=float(input("enter the breadth"))
            print("area of rectangle=length*breadth")
            print("area =",d*e)
        elif b=='semi-circle':
            d=float(input("enter the radius:"))
            print("area=",pi*d*d*0.5)
        elif b=='hexagon':
            c=float(input("enter the side of the shape:"))
            print("area of hexagon= (3√3)side*side/2") 
            print("area=",3*1.7320508075688772935274463415058723669428052*c*c/2)    
        elif b=='cube':
            d=float(input("enter the length of side"))
            e=str(input("if you want to find total surface area, enter 'TSA' or if you want to find lateral surface area, enter 'CSA' "))
            if e=='TSA' or 'tsa':
                print("total surface area of cube=6(side)^2")
                print("toal surface area=",6*d*d)
            elif e=='CSA' or 'csa':
                print("lateral surface area of cube=4(side)^2")
                print("lateral surface area=",4*d*d)
            else:
                print("you overruled the condition")
        elif b=='cuboid':
            c=float(input("enter the mesurement of height(h):"))
            d=float(input("enter the measurement of breadth(b):"))
            f=float(input("enter the measurement of length(l):"))
            e=str(input("if you want to find total surface area, enter 'TSA' or if you want to find lateral surface area, enter 'CSA' "))
            if e=='TSA' or 'tsa':
                print("total surface area of cuboid=2(lb+bh+hl)")
                print("total surface area=",2*f*d+2*d*c+2*f*c)
            elif e=='CSA' or 'csa':
                print("lateral surface area of cuboid=2h(l+b)")
                print("lateral surface area=",2*h*l+2*h*b)
            else:
                print("you overruled the condition")
        elif b=='cone':
            c=float(input("enter the slant height:"))
            d=float(input("enter the height:"))
            f=float(input("enter the base radius:"))
            e=str(input("if you want to find total surface area, enter 'TSA' or if you want to find curved surface area, enter 'CSA' "))
            if e=='TSA' or 'tsa':
                 print("total surface area of cone=πrl+πr^2")
                 print("total surface area=",pi*c*f+pi*f*f)
            elif e=='CSA' or 'csa':
                 print("curved surface area of cone=πrl")
                 print("curved aurface area=",pi*f*c)
            else:
                 print("you overruled the condition")
        elif b=='cylinder':
            c=float(input("enter the radius:"))
            d=float(input("enter the height:"))
            e=str(input("if you want to find total surface area, enter 'TSA' or if you want to find curved surface area, enter 'CSA' "))
            if e=='TSA' or 'tsa':
                print("total surface area of cylinder=2πr(r+h)")
                print("total surface area=",2*pi*c*c+2*pi*c*d)
            elif e=='CSA' or 'csa':
                print("curved surface area of cylinder=2πrh")
                print("curved surface area=",2*pi*c*d)
            else:
                print("you overruled the condition")
        elif b=='sphere':
            c=float(input("enter the radius:"))
            print("area of sphere=4πr^2")
            print("area=",4*pi*c*c)
        elif b=='hemisphere' or 'hemi-sphere':
            c=float(input("enter the radius:"))
            e=str(input("if you want to find total surface area, enter 'TSA' or if you want to find curved surface area, enter 'CSA' "))
            if e=='TSA' or 'tsa':
                print("total surface area of hemisphere=3πr^2")
                print("total surface area=",3*pi*c*c)
            elif e=='CSA' or 'csa':
                print("curved surface area of hemisphere=2πr^2")
                print("curved surface area=",2*pi*c*c)
            else:
                print("you overruld the condition")
        elif b=='frustum':
            c=float(input("enter the radius of the smaller circle(r):"))
            d=float(input("enter the radius of bigger circle(R):"))
            f=float(input("enter the slant height(l):"))
            e=str(input("if you want to find total surface area, enter 'TSA' or if you want to find curved surface area, enter 'CSA' "))
            if e=='TSA' or 'tsa':
                print("total surface area of frustum=πl(R+r)+π(R^2+r^2")
                print("total surface area=",pi*f*d+pi*f*c+pi*d*d+pi*c*c)
            elif e=='CSA' or 'csa':
                print("curved surface area of frustum =πl(R+r)")
                print("curved surface area =",pi*f*d+pi*f*c)
            else:
                print("you overruled the condititon!!")
        else:
            print("you overruled the condition!!")
    elif a=='volume':
        b=str(input("enter the name of shape:"))
        if b=='cube':
            c=float(input("enter the length of the side:"))
            print("volume=side^3")
            print("volume=",c*c*c)
        elif b=='cuboid':
            c=float(input("enter the mesurement of height(h):"))
            d=float(input("enter the measurement of breadth(b):"))
            e=float(input("enter the measurement of length(l):"))
            print("volume of cuboid=l*b*h")
            print("volume=",c*d*e)
        elif b=='cone':
            c=float(input("enter the slant height:"))
            d=float(input("enter the height:"))
            e=float(input("enter the base radius:"))
            print("volume of cone = πr^2*h/3")
            print(pi*e*e*c/3)
        elif b=='cylinder':
            c=float(input("enter the radius:"))
            d=float(input("enter the height:"))
            print("volume of cylinder =πr^2h")
            print("volume=",pi*c*c*d)
        elif b=='sphere':
            c=float(input("enter the radius:"))
            print("volume of sphere = 4/3*πr^3")
            print("volume=",4/3*pi*c*c*c)
        elif b=='hemisphere':
            c=float(input("enter the radius:"))
            print("volume of sphere=2/3 πr^3")
            print("volume=",2/3*pi*c*c*c)
        elif b=='frustum':
            c=float(input("enter the radius of the smaller circle:"))
            d=float(input("enter the radius of the bigger circle:"))
            e=float(input("enter the height:"))
            print("volume of frustum=1/3*π*h(r^2+R^2+R*r")
            print("volume=",1/3*pi*e*c*c+1/3*pi*e*d*d+1/3*pi*e*d*c)
            z=str(input("if you want to do it again enter 'again'"))
        else:
            print("you overruled the condition")
    elif a=='r':
        print("good bye")
    else:
       print("you overruled the condiion!!")
else:
    print("good bye")
    


          
