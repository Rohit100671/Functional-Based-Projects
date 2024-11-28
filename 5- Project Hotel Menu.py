''' *************** RJT Hotel Software ************ '''
menus={1:"Tea",2:"Coffee",3:"Phoha",4:"Idli",5:"Dosa",6:"Samosa"}
price={1:10,2:20,3:25,4:35,5:35,6:30}
print("="*130)
print(" "*50,"Welcome To RJT Hotel's")
print("="*130)
def menu():
    print("""
    -RJT Hotel Menu -
    1.Tea
    2. Coffee
    3. Poha
    4. idli
    5. Dasa
    6. Samosa   """)

def order():
    pass
    
while True:
    menu()
    items=[]
    q=[]
    c=int(input("Enter your Choice: "))
    quantity=int(input("Enter your quantity: "))
    items.append(c)
    q.append(quantity)
    print(items)
    print(q)
    ch=input("Doyou want to continue: ")
    if ch=='n':
        print("="*85)
        print("|{:^20}|{:^20}|{:^20}|{:^20}|".format("Food_Name","Price","Quantity","Amount"))
        print("="*85)
        sum=0
        for i in range(len(items)):
            print("|{:^20}|{:^20}|{:^20}|{:^20}|".format(menus[items[i]],price[q[i]],q[i]),price[q[i]]*q[i])
        sum=sum+price[q[i]]*q[i]
        print(f"Your Total Bill is= {sum}")
    order()
    