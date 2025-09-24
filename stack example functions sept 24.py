myStack = []

def Stack():
    element = input("provide the element you want to add: ")
    myStack.append(element)

def Unstack():
    myStack.pop(myStack[0])

while 1:
    print("Please choose one of the following: ")
    print("1. Enqueue")
    print("2. Dequeue")
    print("5. Quit Application")


    option = input("Please enter your choice here: ")

    if option == "1":
        Stack()

    if option == "2":
        Unstack()

    elif option == "5":
        print("Thank you for using this program!")
        break


