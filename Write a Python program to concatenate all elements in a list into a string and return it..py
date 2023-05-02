#Python program to concatenate all elements in a list into a string and return it.
l1 = ["a","b","c"]
print(type(l1) )
print(l1)
def fun2(l1):
    str1=" ".join(l1)
    return str1
   
str1 = fun2(l1)
print(type(str1))
print(str1)
