# 1. Write a Python program to check the validity of password input by users. Go to the editor Validation:
# a. At least 1 letter between [a-z] and 1 letter between [A-Z].
# b. At least 1 number between [0-9].
# c. At least 1 character from [$#@].
# d. Minimum length 6 characters.
# e. Maximum length 16 characters.
print("Program to check the validity of password input by users. Go to the editor Validation: \n \
    a. At least 1 letter between [a-z] and 1 letter between [A-Z]. \n \
    b. At least 1 number between [0-9]. \n \
    c. At least 1 character from [$#@]. \n \
    d. Minimum length 6 characters. \n \
    e. Maximum length 16 characters.\n")
p = str(input("Enter you password "))
print("\n")
c,s,d,sc = 0,0,0,0
dict = {"Uppercase" : ["Not Ok"] , "Lowercase" : ["Not Ok"] , "Digits" : ["Not Ok"], "Min_length" : ["Not Ok"], "Max_length" : ["Not Ok"], "Speacial_Char" : ["Not Ok"]} 

for i in p:
    if (i.isupper()):
        c += 1
        dict["Uppercase"][0] = "Ok"
    if (i.islower()):
        s += 1 
        dict["Lowercase"][0] = "Ok"
    if (i.isdigit()):
        d += 1
        dict["Digits"][0] = "Ok"
    if i in "$#@" :
        sc += 1 
        dict["Speacial_Char"][0] = "Ok"

if (len(p)>=6):
    dict["Min_length"][0] = "Ok"

if (len(p)<=16):
    dict["Max_length"][0] = "Ok"

if (c>0 and s>0 and d>0 and sc>0 and len(p)>5 and len(p)<17):
    print(f"{p} is valid password"+"\n")
else:
    print(f"{p} is Invalid password. Please check below table for validation results","\n")           

import pandas as pd
df = pd.DataFrame(dict)
print(df)
