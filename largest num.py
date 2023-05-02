#program to find the largest of two numbers without using function.
a = float(input("enter first number\t"))
b = float(input("enter seond number\t"))

if (a>b):
    print(a," is greater than ", b)
else:
    if(a<b):
        print(b," is greater than ", a)
    else:
        if(a==b):
            print("Both number are equal",a)
