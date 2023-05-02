# 1. Write a program to take a sentence from the user and then find count of elements in the sentence. (hint:
# that is calculate how many alphabets how many whitespaces etc.are present)
sent = list(input("enter the sentence "))
# print(sent, len(sen), "".join(sen))
alpha, dig, space = 0,0,0 
for i in sent:
    if i.isupper() or i.islower():
        alpha += 1
    elif i.isdigit():
        dig += 1
    elif i == " ":
        space += 1
print("alphabates= ",alpha)
print("Digits= ",dig)
print("Spaces= ",space)

        
