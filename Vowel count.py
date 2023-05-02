#vowel count
text = str(input("enter string "))
vowels = "aeiouAEIOU"
vowels_count = 0
char = [x for x in text]
for i in char:
    if i in vowels:
        vowels_count += 1

print("Count of Vowels in",text,"is ",vowels_count)        