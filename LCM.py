#logic1
a = int(input("enter first integer "))
b = int(input("enter second integer "))

Fact_a = []
Fact_b = []

for i in range(1,a) :
    if a%i == 0:
        Fact_a.append(i)

for j in range(1,b) :
    if b%j == 0:
        Fact_b.append(j)        

print(f"Factors of {a} excluding {a} = ",Fact_a)   
print(f"Factors of {b} excluding {b} = ",Fact_b)  

common1 = set(Fact_a) & set(Fact_b) # typecast list into SET to perform intesection operation
print("Common elements are ",common1) 
print(type(common1))
GCD = max(common1)
print("GCD = ",GCD)

#Logic2 : HCF × LCM = product of two numbers
LCM_2 = (a*b) / GCD
print("LCM = ",round(LCM_2))
 
#logic3 : LCM of two or more numbers is always greater than or equal to each of the numbers.
minimum = min(a,b)
maximum = max(a,b)
LCM_3 = maximum
while(maximum):
    if (maximum % a == 0) and (maximum % b ==0):
        LCM_3 = maximum
        break  # break is very imp here , otherwise loop will run infinitely
    maximum += 1  #same as maximum = maximum +s1
print("LCM = ",LCM_3)