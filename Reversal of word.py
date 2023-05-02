#Program to reverse the user entered string using fucntion
a = str(input("Enter string to reverse\n"))
def Rev(a):
    return a[-1::-1]
reverse = Rev(a)
print(reverse)