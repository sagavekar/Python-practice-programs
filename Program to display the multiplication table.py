# 1. Program to find Armstrong Number in an interval.
start = int(input("Interval starts at "))
end = int(input("Interval ends at "))
AM = []
for i in range(start,end+1):
    i = str(i)
    index = len(i)
    sum =0
    for j in i:
        j = int(j)
        sum += j**index
    if sum == int(i):
        AM.append(i)

print(AM)
