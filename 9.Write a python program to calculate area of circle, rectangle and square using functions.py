#Python program to calculate area of circle, rectangle and square using functions.
import math
print("Python program to calculate area of circle, rectangle and square using functions\n")
print("Enter 1 for circle")
print("Enter 2 for Rectangle")
print("Enter 3 for Sqr")

def circle():
    r = float(input("enter values of radius\t"))
    A = (math.pi) *r*r
    print("area of circle whose radius is ",r," = ",A," unit sq")

def Rect():
    l = float(input("enter values of lenght\t"))  
    b = float(input("enter values of breadth\t"))    
    A = l*b
    print("area of rectangle = ",A," unit sq")

def Sq():
    l = float(input("enter values of side\t")) 
    A = l*l
    print("area of Square = ",A," unit sq")

choise = int(input("enter your choise number\t"))

if choise==1:
    circle()
elif choise==2:
    Rect()
elif choise==3:
    Sq()
else:        
    print("Your choise is incorrect")