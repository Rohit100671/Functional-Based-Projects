'''************ STUDENT MANAGEMENT SYSTEMS ************* '''

student={1:{"name":"rohit","city":"pune","pass_year":2024,"percentage":72,"cource":"python"}}
print("="*150)
print(" "*60,"STUDENT DETAIL")
print("="*150)
def dashboard():
    print( """
                -Dshboard-
            1. Insert Student Data
            2. Display Studen Data
            3. Update Student Data
            4. Delete Student Data
            5. Student Dta filter
                """)

def insert(rno,name,city,pass_year,per,cource):
    student[rno]={"name":name,"city":city,"pass_year":pass_year,"percentage":per,"cource":cource}
    print(student)



def display():
    print("="*120)
    print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format("Name","City","Passing_Year","Percenntage","Cource"))
    print("="*120)

    for rno in student:
        print("|{:^20}|{:^20}|{:^20}|{:^20}||{:^20}|".format(student[rno]["name"],student[rno]["city"],student[rno]["pass_year"],student[rno]["percentage"],student[rno]["cource"]))
        print("-"*120)

def update():
    rno=int(input("Enetr the Roll no: "))
    if rno in student:
        print( """
                -Update Student Data -
                1. Name
                2. City
                3. Passing _year
                4. Percentage
                5. Corce
                    """)
        ch=int(input("Enter your update items choice: "))
        if ch==1:
            n=input("Enter Name: ")
            student[rno]["name"]=n
            return "Name Updated Successfully..."
        elif ch==2:
            c=input("Enter City: ")
            student[rno]["city"]=c
            return "City Updated Successfully..."
        elif ch==3:
            py=int(input("Enter Pass_year: "))
            student[rno]["pass_year"]=py
            return "Passing_year Updated Successfully..."
        elif ch==4:
            p=eval(input("Enter Percentage: "))
            student[rno]["percenage"]=p
            return "Percentage Updated Successfully..."
        elif ch==5:
            c=input("Enter Coruce: ")
            student[rno]["cource"]=c
            return "Cource Updated Successfully..."
        else:
            return "Invalide Input..."



def delete():
    rno=int(input("Enter roll nu: "))
    if rno in student:
        del student[rno]
        return "Student Data Successfully Delete..."

def datafilter():
        print("""
                - Filter Student Data -
              1. Name
              2. City
              3. Passing_year
              4. Percentage
              5. Cource
                """)
        ch=int(input("Enter your choice to filtering data: "))
        if ch==1:
            fn=input("Enter your name: ")
            print("="*120)
            print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format("Name","City","Passing_Year","Percenntage","Cource"))
            print("="*120)
            for rno in student:
                if fn==student[rno]["name"]:
                    print("|{:^20}|{:^20}|{:^20}|{:^20}||{:^20}|".format(student[rno]["name"],student[rno]["city"],student[rno]["pass_year"],student[rno]["percentage"],student[rno]["cource"]))
                    print("-"*120)

        elif ch==2:
            fc=input("Enter your city: ")
            print("="*120)
            print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format("Name","City","Passing_Year","Percenntage","Cource"))
            print("="*120)
            for rno in student:
                if fc==student[rno]["city"]:
                    print("|{:^20}|{:^20}|{:^20}|{:^20}||{:^20}|".format(student[rno]["name"],student[rno]["city"],student[rno]["pass_year"],student[rno]["percentage"],student[rno]["cource"]))
                    print("-"*120)

        elif ch==3:
            fpy=input("Enter your pass_year: ")
            print("="*120)
            print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format("Name","City","Passing_Year","Percenntage","Cource"))
            print("="*120)
            for rno in student:
                if fpy==student[rno]["pass_year"]:
                    print("|{:^20}|{:^20}|{:^20}|{:^20}||{:^20}|".format(student[rno]["name"],student[rno]["city"],student[rno]["pass_year"],student[rno]["percentage"],student[rno]["cource"]))
                    print("-"*120)
        
        elif ch==4:
            fp=input("Enter your percentage: ")
            print("="*120)
            print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format("Name","City","Passing_Year","Percenntage","Cource"))
            print("="*120)
            for rno in student:
                if fp==student[rno]["percentage"]:
                    print("|{:^20}|{:^20}|{:^20}|{:^20}||{:^20}|".format(student[rno]["name"],student[rno]["city"],student[rno]["pass_year"],student[rno]["percentage"],student[rno]["cource"]))
                    print("-"*120)

        elif ch==5:
            fco=input("Enter your cource: ")
            print("="*120)
            print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format("Name","City","Passing_Year","Percenntage","Cource"))
            print("="*120)
            for rno in student:
                if fco==student[rno]["cource"]:
                    print("|{:^20}|{:^20}|{:^20}|{:^20}||{:^20}|".format(student[rno]["name"],student[rno]["city"],student[rno]["pass_year"],student[rno]["percentage"],student[rno]["cource"]))
                    print("-"*120)

        else:
            return "Invalide Input..."



while True:
    dashboard()
    ch=int(input("Enter your dashboard choice: "))
    if ch==1:
        r=int(input("Enter the roll no: "))
        n=input("Enter the name: ")
        c=input("Enetr the city: ")
        py=int(input("Enter the passing year: "))
        p=eval(input("Enter the percentage: "))
        c=input("Enter the cource: ")
        insert(r,n,c,py,p,c)
    elif ch==2:
        display()
    elif ch==3:
        update()
    elif ch==4:
        delete()
    elif ch==5:
        datafilter()
    else:
        print("Invalid Input")
        break