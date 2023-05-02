# print(chr(65),ord('A'))
n=4 #Driver value
row=0
while(row<=n):
    col =0
    while(col<=((2*n))):
        if col == n-row or col == n+row or row==n:
            print("*",end=" ") 
        else:
            print(" ",end=" ")
        col +=1        
    print()
    row +=1
