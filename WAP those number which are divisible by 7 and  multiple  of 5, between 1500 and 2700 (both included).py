# WAP those number which are divisible by 7 and  multiple  of 5, between 1500 and 2700 (both included)

list1 = []
for i in range(1500,2701):
    if ((i%7==0) and (i%5==0)):
        list1.append(i)
print(list1)

# nl=[]
# for x in range(1500, 2701):
#     if (x%7==0) and (x%5==0):
#         nl.append(str(x))
# print (','.join(nl))