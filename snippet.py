# 1. Write a program to convert a list of multiple integers into a single integer Example where input is [1 ,2 ,3]
# and output is [123]

a = [1,2,3]
a = [str(i) for i in a]
b = "".join(a)
b = int(b)
print(b)
print(type(b))