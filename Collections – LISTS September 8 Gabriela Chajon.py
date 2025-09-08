
'''

myList = [2,4,54,"Justus","Apple"]


myList.append(92)
print(myList)

myList.remove(54)
print(myList)

myList.pop()
print(myList)

'''
'''
myList = ["Red","Green", "Blue"]
myList[1]
myList[2] = "Purple"
print(myList)
'''


print("Welcome!")
myList = []

while True:
    print("Press a number to select the action")
    print("1.Add an element to the list")
    print("2.Remove a specific element from the list")
    print("3.Pop the last element")
    print("4.Display the list ")
    print("5.Quit")

    option = input("Enter your choice: ")

    if option == "1":

     if len(myList) == 0:
       print("No values on list")

     else:
      n1 = input("Enter the element you want to add: ")
      myList.append(n1)

    elif option == "2":

     n2 = input("Enter the number you want to remove: ")
     myList.remove(n2)

    elif option == "3":
     n2 = int(input("Enter the number you want to remove: "))
     myList.pop(n2)


    elif option == "4":
     print("These are the elements of the list: ")
     print(myList)

    elif option == "5":
     print("Thank you for using the app")
     break


