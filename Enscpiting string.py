# 1. Write a program which take a string from the user and decrypt it using shift by 3 method (hint: if user
# enters the value C it should be encrypted as A and so on.)
a = str(input("enter string to enscript "))
enscript = []
for char in a:
    if char == "a":
        enscript.append("y")
    elif char == "A":
        enscript.append("Y")    
    elif char == "b":
        enscript.append("z")
    elif char == "B":
        enscript.append("Z")
    else:        
        enscript.append(chr(ord(char)-2))  #ord() to find ASCII value of character ,  chr() to find character wrt ASCII value
print("".join(enscript))
