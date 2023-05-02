# # 1. Write a program to get whether the element is prime or no.
n = int(input("enter integer to check prime status  "))

#using sympy library --->
import sympy
if sympy.isprime(n):
    print("prime")
else:
    print("non prime")   

#using basic logic and loop --->
flag = 0 #flag zero means initially assume num is prime
for i in range(2,n//2 +1):
    if (n%i == 0):
        flag = 1
        break
# print(flag)
if n ==1 :
    print("non prime")
else:           
    print("prime") if flag == 0 else print("non prime")