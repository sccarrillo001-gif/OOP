class Book:
    def __init__(self):
        self.bookID = ""
        self.bookName = ""
        self.title = ""
        self.author = ""

    def add_book(self):
        self.bookID = input("Enter the Book ID: ")
        self.bookName = input("Enter the Book Name: ")
        self.title = input("Enter the Book Title: ")
        self.author = input("Enter the Author Name: ")

    def display_book(self):
        print("\nBook Information:")
        print("Book ID: ", self.bookID)
        print("Book Name: ", self.bookName)
        print("Title: ", self.title)
        print("Author: ", self.author)


class User:
    def __init__(self):
        self.userID = ""
        self.userName = ""
        self.books_borrowed = []  

    def add_user(self):
        self.userID = input("Enter the User ID: ")
        self.userName = input("Enter the User Name: ")

    def borrow_book(self, book):
        self.books_borrowed.append(book)
        print(self.userName "borrowed" book.title)

    def display_user(self):
        print("\nUser Information:")
        print("User ID: ", self.userID)
        print("User Name: ", self.userName)
        if not self.books_borrowed:
            print("No books borrowed.")
        else:
            print("Books borrowed:")
            for b in self.books_borrowed:
                print(b.title "by" b.author)


# Main Code


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
