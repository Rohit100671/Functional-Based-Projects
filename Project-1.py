'''************ EMPLOYEE SALARY MANEGEMENT SYATEMS **************'''

employee={101:{"name":"rohit","post":"maneger","salary":150000}}
print("="*150)
print(" "*50,"Employee Salry Managements")
print("="*150)

def dashboard():
    print("""
            - Employee Dashboars -
          1. Insert Employee Data
          2. Display Employee Data
          3. Update Employee Data
          4. Delete Employee Data
          5. filter Employee Data    """)


def insert(id,name,post,salary):
    employee[id]={"name":name,"post":post,"salary":salary}
    print(employee)


def display():
    print("="*88)
    print("|{:^20}||{:^20}||{:^20}||{:^20}|".format("Eployee_id","Name","Post","Salary"))
    print("="*88)

    for id in employee:
        print("|{:^20}||{:^20}||{:^20}||{:^20}|".format(id,employee[id]["name"],employee[id]["post"],employee[id]["salary"]))
        print("-"*88)
    else:
        return "Invali Employee_ID."

def update(id):
    print("""
            -Employee Update-
          1. Name
          2. Post
          3. Slary """)
    ch=int(input("Enter your Update Choice: "))
    if ch==1:
        employee[id]["name"]=input("Emter Name: ")
        return "Employee Name Update Successfully..."
    elif ch==2:
        employee[id]["post"]=input("Enter your post: ")
        return "Employee post Update Successfully..."
    elif ch==3:
        employee[id]["salary"]=eval(input("Enter your Salary: "))
        return "Employee Salary Update Successfully..."
    else: 
        return "Invalid Input..."
    
def delete(id):
    del employee[id]
    return "Employee Delated Successfully..."

def datafilter():
    print("""
            - Employee Filter Data -
          1. Name
          2. Post
          3. Salary """)
    ch=int(input("Enter your choice to filter data: "))
    if ch==1:
        fn=input("Entwr the name: ")
        print("="*88)
        print("|{:^20}||{:^20}||{:^20}||{:^20}|".format("Eployee_id","Name","Post","Salary"))
        print("="*88)

        for id in employee:
            if fn==employee[id]["name"]:
                print("|{:^20}||{:^20}||{:^20}||{:^20}|".format(id,employee[id]["name"],employee[id]["post"],employee[id]["salary"]))
                print("-"*88)
        
    if ch==2:
        fpo=input("Entwr the post: ")
        print("="*88)
        print("|{:^20}||{:^20}||{:^20}||{:^20}|".format("Eployee_id","Name","Post","Salary"))
        print("="*88)

        for id in employee:
            if fpo==employee[id]["post"]:
                print("|{:^20}||{:^20}||{:^20}||{:^20}|".format(id,employee[id]["name"],employee[id]["post"],employee[id]["salary"]))
                print("-"*88)

    if ch==3:
        fs=input("Entwr the salary: ")
        print("="*88)
        print("|{:^20}||{:^20}||{:^20}||{:^20}|".format("Eployee_id","Name","Post","Salary"))
        print("="*88)

        for id in employee:
            if fs==employee[id]["salary"]:
                print("|{:^20}||{:^20}||{:^20}||{:^20}|".format(id,employee[id]["name"],employee[id]["post"],employee[id]["salary"]))
                print("-"*88)
            
    else: 
        return "invalid Imput..."


while True:
    dashboard()
    ch=int(input("Enetr your Dashboard Choice: "))
    if ch==1:
        e_id=int(input("Enter Employee_ID: "))
        e_n=input("Emter the Employee Name: ")
        e_po=input("Enter the EmployeePost: ")
        e_s=eval(input("Enter Employee Salary: "))
        insert(e_id,e_n,e_po,e_s)

    elif ch==2:
        display()
    elif ch==3:
        e_id=int(input("Enter the Employee_ID: "))
        update(e_id)
    elif ch==4:
        e_id=int(input("Enter the Employee_ID: "))
        delete(e_id)
    elif ch==5:
        datafilter()
    else:
        print("Invalide Input...")
        break