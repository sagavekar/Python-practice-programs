#1. Write a program to check common letters in two input String?
a = str(input("enter first string  "))
b = str(input("enter second string  "))
s1 = set() # create an empty set
s2 = set() # create an empty set

for i in a:
    s1.add(i)
for j in b:
    s2.add(j)

if (s1 & s2):
    # common = s1 & s2
    # common = s1.intersection(s2
    print("Common elements from entered two strings = ",s1 & s2)
else:
    print("No common elements")    