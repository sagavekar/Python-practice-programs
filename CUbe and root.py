# 1. Write a program to take a list from the user and find the cube and square root of every number in it.
l = str(input("enter integer separated by spaces "))
cube,sroot = [],[]
l = list(l.split())
l = [int(x) for x in l] #python_lists_comprehension
for i in l:
    cube.append(int(i)**3)
    sroot.append(int(i)**0.5)
print("Given array= ",l)
print(" Cube= ",cube) 
print(" sroot= ",sroot)   
