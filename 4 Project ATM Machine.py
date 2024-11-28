'''********* ATM Machine Software with the functional programing ***************'''
bank={1010:10000,1011:11000,1012:12000,1013:13000,1014:14000,1015:15000,16:16000,1017:17000,1018:18000,1019:19000,1020:20000}
print("="*130)
print(" "*50," Welcome... RJT Bank ATM ")
print("="*130)

def desktop():
    print("""
    - ATM Desktop -
    1. Withdral Amount
    2. Deposit Amount
    3. Balance Inquiry
    4. Exist Process """)

def withdrawl(pin,wa):
    totalwa=bank[pin]-wa
    bank[pin]=totalwa

def deposit(pin,dep):
    totaldep=bank[pin]+dep
    bank[pin]=totaldep
    print("Deposit Successfull...")

def balance(pin):
    print("Your Account Balanc is",bank[pin])


def exist():
    print("Thank You! Visit Again...")



while True:
    insertcard=input("Enter your card(yes/no): ")
    if insertcard=='yes':
        desktop()
        ch=int(input("Ente your choise: "))
        if ch==1:
            p=int(input("enter the pin: "))
            if p in bank:
                w=eval(input("Enter Amount You can Withrawliing: "))
                if w<bank[p]:
                    print("Withdrawl Successful...")
                else:
                    print("Insufficient Amount...")
            else:
                print("Invalid Pin Inserted...")
            withdrawl(p,w)

        elif ch==2: 
            p=int(input("Enter your pin: "))
            d=int(input("Enter your deposit amount: "))
            deposit(p,d)
        
        elif ch==3:
            p=int(input("Enter the pin: "))
            balance(p)
        
        elif ch==4:
            exist()
            break
    else:
        print("Please insert your card...")
        break