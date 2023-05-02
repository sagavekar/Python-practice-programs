#Armstrong number
n = int(input("enter integer "))
n = str(n)
x = len(n)
sum = 0
for i in n:
    i = int(i)
    sum += i**x

if sum == int(n):
    print(f"{n} is Armstrong number")
else:
    print(f"{n} is not Armstrong number")