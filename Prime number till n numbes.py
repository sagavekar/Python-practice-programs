# 1. Write a program to get the prime no up to n. n should be taken from the user.
n = int(input("Till which integer you want to find prime numbers  "))
prime = []
for i in range(2,n+1):
    flag = 0 # assume that i is prime , flag = 1 mean division successfull and hence non-prime
    for j in range(2,i//2 +1):
        if i%j == 0:
            flag = 1
            break
    if flag == 0:
        prime.append(i)
            
print(prime)

