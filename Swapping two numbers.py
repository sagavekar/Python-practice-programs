#swapping of two numbers using function call

a = float(input("enter first number i.e a\t"))
b = float(input("enter second number i.e b\t"))
def swap(a,b):
    a,b = b,a
    return a,b

a,b = swap(a,b)
print("first number becomes "+str(a))
print("Second number becomes "+str(b))