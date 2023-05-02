#1. Program to count the number of each vowel.
text = str(input("enter string "))
vowels = "aAeEiIoOuU"
vowels_found = []
char = [x for x in text]
for i in char:
    if i in vowels:
        vowels_found.append(i)
for j in range(0,len(text)):    
   
    print(f"{vowels[j] , vowels[j+1]} :", vowels_found.count(vowels[j])+vowels_found.count(vowels[j+1]))
