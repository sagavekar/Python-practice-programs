print("A year is a leap year if the following conditions are satisfied: /n \
The year is multiple of 400./n \
The year is multiple of 4 and not multiple of 100.")
y =int(input("enter yeat to check "))
if ( y%4==0  and y%100 != 0) or (y%400 ==0):
    print("Leap year")
else:
    print("Non-leap year")    