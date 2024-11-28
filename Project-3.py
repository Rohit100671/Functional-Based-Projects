'''************** Library Books Managment Systems *************'''
books={1101:{"book_name":"python","author":"Rohit","price":250,"language":"english"}}
print("="*135)
print(" "*50,"Welcome... To RJT Library")
print("="*135)

def dashboard():
    print("""
          - Lirary Dashboard -
          1. Add Books
          2. Display Books
          3. Access Books """)    

def add(code,name,author,price,language):
    books[code]={"book_name":name,"author":author,"price":price,"language":language}
    print(books)

def dispaly():
    print("-"*110)
    print("|{:^20}||{:^20}||{:^20}||{:^20}||{:^20}|".format("BookC_Code","Book_Name","Book_Author","Book_Price","Book_Lanuage"))
    print("-"*110)

    for code in books:
        print("|{:^20}||{:^20}||{:^20}||{:^20}||{:^20}|".format(code,books[code]["book_name"],books[code]["author"],books[code]["price"],books[code]["language"]))
        print("-"*110)

def access(code):
    del books[code]

while True:
    dashboard()
    ch=int(input("Enter your Choice: "))
    if ch==1:
        c=int(input("Enter the book code:"))
        n=input("Enter the book name: ")
        a=input("Enter the Book author: ")
        p=eval(input("Enter the book Price: "))
        l=input("Enter the book language: ")
        add(c,n,a,p,l)
    elif ch==2:
        dispaly()

    elif ch==3:
        c=int(input("Enter the book code: "))
        access(c)
        print("Your Access book Successfully...")

 
    else:
        print("Invalid Input...")