from database1 import SessionLocal
from models import Book,Member,Issue
from collections import defaultdict
# details = []
# persons=[]
# mtobid=defaultdict(list)


print("\n===== Library Management System =====")
print("1. Add Book")
print("2. View Books")
print("3. Search Book")
print("4. Add Member")
print("5. View Members")
print("6. Issue Book")
print("7. Return Book")
print("8. Delete Book")
print("9. Exit")
# def Enter_details():
#     book={
#         "Book_id":int(input("Enter Book id:")),
#         "Book_Name":(input("Enter Book Name:")),
#         "Book_Author":(input("Enter Author Name:"))
# }
#     details.append(book)

def Enter_details():
    title = input("Enter Book Name: ")
    author = input("Enter Author Name: ")

    db = SessionLocal()

    book = Book(
        title=title,
        author=author
    )

    db.add(book)
    db.commit()
    db.refresh(book)

    print("Book added successfully!")
    print("Book id:", book.id)

    db.close()
def add_members():
    name = input("Enter your name: ")

    db = SessionLocal()

    member = Member(
        name=name
    )

    db.add(member)
    db.commit()
    db.refresh(member)

    print("Member added successfully!")
    print("Member ID:", member.id)

    db.close()
    


while True:

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Adding Book")
        Enter_details()

    # elif choice == 2:
    #     print("View Books")
    #     print("Book Details are:",details)
    elif choice == 2:
        print("View Books")

        db = SessionLocal()

        books = db.query(Book).all()

        for book in books:
            print("Book ID:", book.id)
            print("Book Name:", book.title)
            print("Author:", book.author)
            print("--------------------")

        db.close()

    

    # elif choice == 3:
    #     s_id=int(input("Enter Book id for search:"))
    #     print("Search Book")
    #     book_found=False
    #     for i in range(len(details)):
    #        d=details[i]
    #        d_id=d["Book_id"]
    #        if d_id==s_id:
    #            print("Our book details:",d)
    #            book_found=True
    #            break
    #     if book_found==False:
    #            print("No Book with:",s_id)

    elif choice == 3:
        print("Search Book")

        s_id = int(input("Enter Book id for search: "))

        db = SessionLocal()

        book = db.query(Book).filter(Book.id == s_id).first()

        if book:
            print("Book ID:", book.id)
            print("Book Name:", book.title)
            print("Author:", book.author)
        else:
            print("No Book with:", s_id)

        db.close()

    elif choice == 4:
        print("Add Member")
        add_members()

    

    # elif choice == 5:
    #     print("View Members")
    #     print("persons are:",persons)


    elif choice == 5:
        print("View Members")

        db = SessionLocal()

        members = db.query(Member).all()

        for member in members:
            print("Member ID:", member.id)
            print("Member Name:", member.name)
            print("--------------------")

        db.close()


    # elif choice == 6:
    #      print("Issue Book")
    #      username=input("Enter your Name:")
    #      if username in persons:
    #         print(details)
    #         print("select your bookid")
    #         u_id=int(input("Enter book id:"))
    #         book_found = False
    #         for book in details:
    #             if book["Book_id"] == u_id:
    #                 book_found = True
    #                 break
    #         if book_found == False:
    #             print("Book is not there with this id:",u_id)
    #         else:
    #             mtobid[u_id].append(username)
    #             print(mtobid)     

    elif choice == 6:
        print("Issue Book")

        username = input("Enter your Name: ")
        u_id = int(input("Enter book id: "))

        db = SessionLocal()

        member = db.query(Member).filter(Member.name == username).first()

        if not member:
            print("Member is not found:", username)
        
        else:
            book = db.query(Book).filter(Book.id == u_id).first()

            if not book:
                print("Book is not there with this id:", u_id)
 
            else:
                existing_issue = db.query(Issue).filter(
                    Issue.book_id == book.id
                ).first()

                if existing_issue:
                    print("Book is already issued!")
                else:
                    issue = Issue(
                        member_id=member.id,
                        book_id=book.id
                    )

                    db.add(issue)
                    db.commit()

                    print("Book issued successfully!")
           
    # elif choice == 7:
    #     print("Return Book")
    #     name=input("Enter your Name:")
    #     id=int(input("Enter your Book id:"))
    #    # print(mtobid[id])
    #     if name in mtobid[id]:
    #         print("Return your book")
    #         mtobid[id].remove(name)
    #         print("Remove Name is:",name) 
    #     else:
    #         print("You have already Returned")


    elif choice == 7:
        print("Return Book")

        name = input("Enter your Name: ")
        book_id = int(input("Enter your Book id: "))

        db = SessionLocal()

        member = db.query(Member).filter(Member.name == name).first()

        if not member:
            print("Member is not found:", name)
        else:
            issue = db.query(Issue).filter(
                Issue.member_id == member.id,
                Issue.book_id == book_id
            ).first()

            if issue:
                db.delete(issue)
                db.commit()
                print("Book returned successfully!")
            else:
                print("You have already returned this book.")

        db.close()
        
    # elif choice == 8:
    #     print("Delete Book")
    #     id1=int(input("Enter Book id you want to delete:"))
    #     for i in range(len(details)):
    #         if details[i]["Book_id"]==id1:
    #             details.pop(i)
    #             print(details)
    elif choice == 8:
        print("Delete Book")

        id1 = int(input("Enter Book id you want to delete: "))

        db = SessionLocal()

        book = db.query(Book).filter(Book.id == id1).first()

        if not book:
            print("No Book with:", id1)

        else:
            existing_issue = db.query(Issue).filter(
                Issue.book_id == book.id
            ).first()

            if existing_issue:
                print("Book is currently issued. Return the book first.")

            else:
                db.delete(book)
                db.commit()
                print("Book deleted successfully!")

        db.close()
        
            

    elif choice == 9:
        print("Thank you for using Library Management System")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 9.")
    