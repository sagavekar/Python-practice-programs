"""Accept the marks obtained by the 3 students for subjects of Python, Statistics, Machine Learning, Deep
Learning, Big-Data also all marks are out of 100. Find the sum and percentage of the for all students and
display the name and marks of the first rank holder."""
import pandas as pd 
dict = {s
    "Student Name" : [],
    "Python" : [],
    "Statistics" : [],
    "Machine Learning" : [],
    "Deep Learning" : [],
    "Big data" : [],
    "sum" : [],
    "Perc" : []
}

print("Enter 3 student name and their marks in respective subjects ")

n = 3
for i in range(0,n):
    dict["Student Name"].append(str(input("Enter student name ")))
    dict["Python"].append(int(input("Enter Python marks ")))
    dict["Statistics"].append(int(input("Enter Statistics marks ")))
    dict["Machine Learning"].append(int(input("Enter Machine learning marks ")))
    dict["Deep Learning"].append(int(input("Enter Deep learning marks ")))
    dict["Big data"].append(int(input("Enter Big data marks ")))
    print("\n")
    # To calculate percentage obtained out of 500 marks
    sum = 0
    pc = 0
    sum = dict["Python"][i] + dict["Statistics"][i] + dict["Machine Learning"][i] + dict["Deep Learning"][i] + dict["Big data"][i]
    pc = (float(sum)/500)*100
    dict["sum"].append(sum)
    dict["Perc"].append(pc)



df = pd.DataFrame(dict)

print("Table of student and marks is given below \n",df)


max_perc = max(dict["Perc"])
max_marks = max(dict["sum"])


index_of_highest_perc = dict["Perc"].index(max_perc)
# print(index_of_highest_perc)
print("First rank holder is ",dict["Student Name"][index_of_highest_perc],f" with max marks {max_marks} and {max_perc} percentage !")
