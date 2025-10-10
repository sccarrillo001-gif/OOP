class Book:
    def __init__(self, bid, btitle, bauthor, bpublisher, byear):
        self.bookID = bid
        self.book_title = btitle
        self.author_id = bauthor
        self.publisher = bpublisher
        self.year_of_publication = byear


    def add_book(self):
        self.bookID = input("Enter the Book ID: ")
        self.book_title = input("Enter the Book Title: ")
        self.author_id = input("Enter the Book author id: ")
        self.publisher = input("Enter the Book publisher: ")
        self.year_of_publication = input("Enter the year of publication: ")

    def display_book(self):
        print("Book Information:")
        print("Book ID: ", self.bookID)
        print("Book Title: ", self.book_title)
        print("Author ID: ", self.author_id)
        print("Publisher: ", self.publisher)
        print("Year of publication: ", self.year_of_publication)



class User:
    def __init__(self):
        self.userID = ""
        self.userName = ""
        self.password = ""
        self.address = ""
        self.email_id = ""
        self.books_borrowed = []

    def add_user(self):
        self.userID = input("Enter the User ID: ")
        self.userName = input("Enter the User Name: ")
        self.password = input("Enter the User password: ")
        self.address = input("Enter the User address: ")
        self.email_id = input("Enter the User email id: ")

    def borrow_book(self, book):
        self.books_borrowed.append(book)
        print(self.userName, "borrowed", book.title)

    def display_user(self):
        print("User Information:")
        print("User ID: ", self.userID)
        print("User Name: ", self.userName)
        if not self.books_borrowed:
            print("No books borrowed.")
        else:
            print("Books borrowed:")
            for b in self.books_borrowed:
                print("Books borrowed: ", b.title, "by", b.author)

class Author:
    def __init__(self):
                        self.author_id = ""
                        self.author_name = ""
                        self.affiliation = ""
                        self.country = ""
                        self.phone = ""
                        self.email_id = ""


    def add_user(self):
                    self.userID = input("Enter the User ID: ")
                    self.userName = input("Enter the User Name: ")
                    self.password = input("Enter the User password: ")
                    self.address = input("Enter the User address: ")
                    self.email_id = input("Enter the User email id: ")

# Main Code
            print("Welcome!")

            while True:
                print("Please choose one of the following: ")
                print("1. Create object")
                print("2. Project Closure")
                print("3. Project Progress Update an employee")
                print("4. Print a specific project")
                print("4. Print all projects")
                print("5. Quit Application")

b1 = Book()
b2 = Book()
b3 = Book()
b4 = Book()
b5 = Book()

u1 = User()
u2 = User()


u1.add_user()
u2.add_user()


b1.add_book()
b2.add_book()
b3.add_book()
b4.add_book()
b5.add_book()


u1.borrow_book(b1)
u1.borrow_book(b3)
u2.borrow_book(b2)
u2.borrow_book(b4)
u2.borrow_book(b5)


u1.display_user()
u2.display_user()