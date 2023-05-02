#WAP to find area of traingle using function
length = float(input("enter length of triangle\n"))
breadth = float(input("enter breadth of triangle\n"))

def area(l,b):   #defining function with arguments
    areais = 0.5*l*b 
    return areais

print("area of traingle is "+str(area(length,breadth))+" sq. unit")