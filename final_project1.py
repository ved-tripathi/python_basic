name1=str(input("enter the 1st name:"))
name2=str(input("enter the 2nd name:"))
name3=str(input("enter the 3rd name:"))
def name(name1,name2,name3):
	name1.capitalize()
	name2.capitalize()
	name3.capitalize()
	a=list(name1.capitalize())
	b=list(name2.capitalize())
	c=list(name3.capitalize())
	d=[a,b,c]
	return d
print(name(name1,name2,name3))

    


