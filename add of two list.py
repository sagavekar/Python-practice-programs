# 1. Write a program to take two lists from the user and add the element present at same index from two list
# and create a third list. for e.g. element at index 1 of list 1 should get added with element at index 1 of list
# 2 and so on
n = int(input("how many element you would like to add in list  "))
l1 , l2, l3 = [] , [] , []
for i in range(0,n):
    x = int(input("enter number of first list "))
    l1.append(x)
    y = int(input("enter number of second list "))
    l2.append(y)
    l3.append(x+y)

print(f"list1 is {l1}   list2 is {l2}  combine sum list3 is {l3} ")   