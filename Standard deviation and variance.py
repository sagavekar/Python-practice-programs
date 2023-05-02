# 1. Write a program to calculate standard deviation and variance. Assume the data in the list.
num = str(input("enter number separated by space \n"))
num = list(num.split())  # separating the elements by space
num = [float(x) for x in num] # convertnig element into float using list comprehension
# print(type(num),num)

#using numpy library
import numpy
print(num)
print("variance = ",numpy.var(num))
print("standard deviation = ",numpy.std(num))

#using common logic
import statistics
mean_num = statistics.mean(num) # to find avg of all elements in list
sq = []
for i in num:
    sq.append((i-mean_num)**2)

var = statistics.mean(sq)
print("variance= ",var)
print("standart deviation= ",var**0.5)
