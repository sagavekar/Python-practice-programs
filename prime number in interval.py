print("Program to check prime numbers in an interval.")
start = int(input("Interaval starts from  "))
end = int(input("Interval ends at "))
prime = []
for i in range(start,end+1):
    flag = 0 # assume that i is prime , flag = 1 mean division successfull and hence non-prime
    for j in range(2,i//2 +1):
        if i%j == 0:
            flag = 1
            break
    if flag == 0:
        prime.append(i)
            
print(prime)

