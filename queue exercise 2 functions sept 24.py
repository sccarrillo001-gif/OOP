myQueue = []

def Enqueue():
    element = input("provide the element you want to add: ")
    myQueue.append(element)

def Dequeque():
    myQueue.remove(myQueue[0])

while 1:
    print("Please choose one of the following: ")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Quit Application")


    option = input("Please enter your choice here: ")

    if option == "1":
        Enqueue()

    if option == "2":
        Dequeque()

    elif option == "3":
        print("Thank you for using this program!")
        break


