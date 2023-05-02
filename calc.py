#Write a program using functions to create a calculator (only +, -, * and /) operations should be performed.
print("Note :- you can perform opertaions '+, -, * and / ' in this calc \n only 2 number can be entered ")
a = float(input("enter first number "))
b = float(input("enter second number "))
def  add(a,b):
    return(a + b)
def sub(a,b):
    return(a-b)
def mul(a,b):
    return(a*b)
def div(a,b):
    return(a/b)
op = int(input("which operation you want to perform ?\n 1.for addition \n 2. for sub \n 3. for mult \n 4.for div s" ))

if op == 1:
    print(f"{a}+{b} = {add(a,b)}")    
elif op == 2:
    print(f"{a}-{b} = {sub(a,b)}")
elif op == 3:
    print(f"{a}*{b} = {mul(a,b)}")
elif op == 4:
    print(f"{a}/{b} = {div(a,b)}")                         
    