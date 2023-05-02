#mean mediun mod  by import module statistics
import statistics
a = str(input("Enter numbers separated by space"))
b = a.split()
b = [int(i) for i in b]  
print(b)
print("mean= ",statistics.mean(b))
print("mode= ",statistics.mode(b))
print("median= ",statistics.median(b))