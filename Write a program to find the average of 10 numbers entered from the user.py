#Write a program to find the average of 10 numbers entered from the user.

print("program to find the average of 10 numbers entered from the user\n")
str1 = str(input("enter 10 numeber separated by single space   "))
print(type(str1))
print(str1) 

list1  = str1.split()
print(type(list1))
print(list1)

# for i in range(0, len(list1)):
#     list1[i] = int(list1[i]) # typecasting of list elements
count = 0
for i in range(0, len(list1)):
    count += int(list1[i])

avg = count /10
print("sum of all entered integers is ", avg)
