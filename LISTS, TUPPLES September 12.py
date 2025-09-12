print("Welcome!")
myList = []

while True:
    print("Press a number to select the action")

    print("1.Add an element to the list")
    print("2.Remove a specific element from the list")
    print("3.Replace an element from the list")
    print("4.Sort the elements in the list ")
    print("5.Reverse the elements in the list")
    print("6.Print the elements in the list")
    print("7.Exit")

    option = input("Enter your choice: ")

    if option == "1":
      n1 = int(input("Enter the element you want to add: "))
      myList.append(n1)

    elif option == "2":

     if len(myList) == 0:
       print("No values on list")

     n2 = input("Enter the number you want to remove: ")
     myList.remove(n2)

    elif option == "3":
        x = int(input("Enter the position of the element to be replaced: "))
        new_element = int(input("Enter the number you want to replace: "))
        myList[x] = new_element

    elif option == "4":
        myList.sort()
        print("These are the elements sorted: ", myList)


    elif option == "5":
        myList.reverse()
        print("These are the elements reversed: ", myList)


    elif option == "6":
        print("These are the elements of the list: ")
        print(myList)

    elif option == "7":
     print("Thank you for using the app")
     break

