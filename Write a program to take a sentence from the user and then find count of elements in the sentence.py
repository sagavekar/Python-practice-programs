#Write a program to take a sentence from the user and then find count of elements in the sentence
list1 = list(input("enter sentence \n"))
list2 = []
for i in range(0,len(list1)):
    if list1[i] not in list2:
        list2.append(list1[i])
print(list2)
for j in range(0, len(list2)):
    x = list1.count(list2[j])
    print(list2[j]," : ",x)        


