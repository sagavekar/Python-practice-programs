l = str(input("Enter numbers separated by spaces "))
l = set(l.split()) # use SET method to avoid duplicate elements
l = list(l)
l = [float(i) for  i in l]
l.sort() # sorting 
if len(l)>1:
    print("second largest number is = ", l[1])
else:
    print("Only one element exist in list")    