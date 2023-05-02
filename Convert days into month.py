# 46. Program to convert days to months and days.
d = int(input("enter number of days "))
print("Assumption : /n 1. Each month contains 30 days")
rem = d % 30
m = d // 30
print(f"{m} Month(s) and {rem} day(s)")
