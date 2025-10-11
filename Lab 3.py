class Book:
    def __init__(self):
        self.bookID = ""
        self.book_title = ""
        self.author_id = ""
        self.author = ""
        self.publisher = ""
        self.year_of_publication = 0

    def add_book(self):
        self.bookID = input("Enter the Book ID: ")
        self.book_title = input("Enter the Book Title: ")
        self.author_id = input("Enter the Author ID: ")
        self.publisher = input("Enter the Publisher: ")
        self.year_of_publication = int(input("Enter the Year of Publication: "))

    def display_book(self):
        print("Book Information:")
        print("Book ID:", self.bookID)
        print("Book Title:", self.book_title)
        print("Author:", self.author)
        print("Publisher:", self.publisher)
        print("Year of Publication:", self.year_of_publication)


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
        self.password = input("Enter the Password: ")
        self.address = input("Enter the Address: ")
        self.email_id = input("Enter the Email ID: ")

    def borrow_book(self, book):
        self.books_borrowed.append(book)
        print(self.userName, "borrowed", book.book_title)

    def display_user(self):
        print("User Information:")
        print("User ID:", self.userID)
        print("User Name:", self.userName)
        print("Email:", self.email_id)
        if not self.books_borrowed:
            print("No books borrowed.")
        else:
            print("Books borrowed:")
            for b in self.books_borrowed:
                print("-", b.book_title, "by", b.author)


class Author:
    def __init__(self):
        self.author_id = ""
        self.author_name = ""
        self.affiliation = ""
        self.country = ""
        self.phone = ""
        self.email_id = ""

    def add_author(self):
        self.author_id = input("Enter Author ID: ")
        self.author_name = input("Enter Author Name: ")
        self.affiliation = input("Enter Affiliation: ")
        self.country = input("Enter Country: ")
        self.phone = input("Enter Phone: ")
        self.email_id = input("Enter Email ID: ")

    def display_author(self):
        print("Author Information:")
        print("Author ID:", self.author_id)
        print("Author Name:", self.author_name)
        print("Affiliation:", self.affiliation)
        print("Country:", self.country)
        print("Phone:", self.phone)
        print("Email:", self.email_id)


# Main Code
books = {}
authors = {}
users = {}

print("=Welcome")

while True:
    print("1. Add Author")
    print("2. Add Book")
    print("3. Add User")
    print("4. Borrow Book")
    print("5. Display All Authors")
    print("6. Display All Books")
    print("7. Display All Users")
    print("8. Quit")

    option = input("Enter your choice: ")

    if option == "1":
        a = Author()
        a.add_author()
        authors[a.author_id] = a
        print("Author", a.author_name, "added")

    elif option == "2":
        b = Book()
        b.add_book()
        if b.author_id in authors:
            b.author = authors[b.author_id].author_name
            books[b.bookID] = b
            print("Book", b.book_title, "added")
        else:
            print("Author not found")

    elif option == "3":
        u = User()
        u.add_user()
        users[u.userID] = u
        print("User", u.userName, "added")

    elif option == "4":
        user_id = input("Enter User ID: ")
        book_id = input("Enter Book ID: ")
        if user_id in users and book_id in books:
            users[user_id].borrow_book(books[book_id])
        else:
            print("User or Book not found")

    elif option == "5":
        if authors:
            for a in authors.values():
                a.display_author()
        else:
            print("No authors available")

    elif option == "6":
        if books:
            for b in books.values():
                b.display_book()
        else:
            print("No books available")

    elif option == "7":
        if users:
            for u in users.values():
                u.display_user()
        else:
            print("No users available")

    elif option == "8":
        print("Thank you for using the program")
        break
