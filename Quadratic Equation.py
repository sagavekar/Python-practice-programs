#WAP to solve Qaudratic Equation using function
print("Standard Qaudratic equation look like\n ax^2 + bx + c = 0"+"\n Please input coefficients one by one")
a = float(input("Enter value of a\t"))
b = float(input("Enter value of b\t"))
c = float(input("Enter value of c\t"))
def Q(a,b,c):
    discriminant = ((b**2)-(4*a*c))
    m = discriminant**0.5
    if discriminant==0:
        x1 = (-b)/(2*a)
        return x1
    if discriminant>0: 
        x1 = (-b+m)/(2*a)
        x2 = (-b-m)/(2*a)
        solution = [x1,x2]
        return solution
    if discriminant<0:
        discriminant = discriminant*-1
        m = discriminant**0.5
        f1 = (-b/(2*a))
        f2 = (m/(2*a))
        x1 = str(f1)+" + "+str(f2)+"i"
        x2 = str(f1)+" - "+str(f2)+"i"
        solution = [x1,x2]
        return solution

print(Q(a,b,c))


