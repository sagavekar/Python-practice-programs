#WAP to find sq root of number
a = float(input("enter number to find its square root\n"))
def sqroot(a):
    sqroot = a**0.5 
    return sqroot

print(round(sqroot(a),5))  # Round function to restict the floating points