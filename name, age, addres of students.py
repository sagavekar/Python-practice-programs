# Write a Python program to take the user information for n students details like name, age, address and
# print them on different lines.
import pandas as pd
dict = {
    "name"     :     [],
    "age"      :     [],
    "address"  :     []
}
n = int(input("How many student data you want to add? "))
print(f"Now loop will run {n} times " + "\n")

for i in range(0,n):
    name = str(input("Enter student name "))
    dict["name"].append(name)

    age = int(input("Enter student age "))
    dict["age"].append(age)
    
    address = str(input("Enter student address "))
    dict["address"].append(address)

    print("\n") 

print("dictionary becomes = ",dict)

df = pd.DataFrame(dict)
print(df)
