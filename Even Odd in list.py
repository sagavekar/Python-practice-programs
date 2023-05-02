# 1. Write a program to find even and odd numbers from the given list
str1 = str(input("Enter integers separated by space "))
l1 = list((str1.split()))
print(l1)
l1 = [int(x) for x in l1] #python_lists_comprehension
even,odd = [], []
print(type(l1[0]))
for i in l1:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("Even = ",even,"\n","Odd = ",odd)            