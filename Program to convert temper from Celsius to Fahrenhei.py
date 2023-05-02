#Program to convert temperature from Celsius to Fr. Formula : c/5 = f-32/9

Celsius = float(input("Enter temp in celsius\n"))

def convert(Celsius):
    return (((9/5)*Celsius) + 32)

Fr = (convert(Celsius))

print(round(Fr,3))  #round function is used to limit the floating point to 3 decimals
  
