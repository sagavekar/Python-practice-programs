#Python program to imitate bank transactions like deposit, withdrawal and check balance. [Hint: Create different functions for different type of transactions.
current_bal = 50
print("welcom to bank! \nselect operation from below")
print("enter\n 1 for balance check\n 2 for deposit \n 3 for withdrawal")
select = int(input("enter option\t"))

def balance_check(select,current_bal):
   print("Balance is in RS",current_bal)

def deposit(select,current_bal):
    addi = int(input("how much amount of money you want to deposit ?\t"))
    current_bal = current_bal + addi
    print("New balance is ",current_bal)
    
def withdrawal(select,current_bal):
    sub = int(input("how much amount of money you want to withdrw ?\t"))
    if  current_bal<=0 or current_bal-sub<=0:
        print("Insuff balance ",current_bal, "you cant withdrw")
    else:
        current_bal = current_bal - sub
        print("New balance is ",current_bal)

if (select==1):
    balance_check(select,current_bal)
else:
    if(select==2):
        deposit(select,current_bal)
    else:
        if(select==3):
            withdrawal(select,current_bal)

