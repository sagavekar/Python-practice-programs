#logic1
a = int(input("enter first integer "))
b = int(input("enter second integer "))

Fact_a = []
Fact_b = []

for i in range(1,a+1) :
    if a%i == 0:
        Fact_a.append(i)

for j in range(1,b+1) :
    if b%j == 0:
        Fact_b.append(j)        

print("Factors of",a,"= ",Fact_a)   
print("Factors of",b,"= ",Fact_b)  

common1 = set(Fact_a) & set(Fact_b) # typecast list into SET to perform intesection operation
print("Common elements are ",common1) 
print(type(common1))

print("GCD = ",max(common1))

#logic2
minimum = min(a,b)
maximum = max(a,b)
GCD_by_logic2 = 1
for i in range(1, minimum + 1):
    if (a%i==0) and (b%i==0):
        GCD_by_logic2 = i
print("GCD = ", GCD_by_logic2)

#logic3
import math
print("GCD = ", math.gcd(a,b))   # math.gcd is case sensative