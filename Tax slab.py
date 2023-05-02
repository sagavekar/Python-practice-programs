dict = {"salary":"Tax rate","upto 2,00,000":" nil","2,00,001-5,00,000":" 10%","Above 5,00,000":" 20%"}
for key, value in dict.items():
    print(f'{key: <25}{value}') # 25 represents the gap between 2 columns here

salary = int(input("\nEnter gross salary \n"))
tax = 0 if salary<=200000 else ( salary*0.1 if (salary>=200001 and salary<=500000) else salary*0.2 )
print("Tax = ",tax)