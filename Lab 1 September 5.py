print("Welcome!")

while 1:
    print("Press a number to select the action")
    print("1.Addition")
    print("2.Substraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Quit")

    option = input("Enter your choice: ")


    if option == "1":
        n1 = int(input("Enter the first number: "))
        n2 = int(input("Enter the second number: "))
        result = n1+n2
        print(n1, "+", n2, "=", result)


    elif option == "2":
        n1 = int(input("Enter the first number: "))
        n2 = int(input("Enter the second number: "))
        result = n1-n2
        print(n1, "-", n2, "=", result)

    elif option == "3":
        n1 = int(input("Enter the first number: "))
        n2 = int(input("Enter the second number: "))
        result = n1 * n2
        print(n1, "*", n2, "=", result)

    elif option == "4":
        n1 = int(input("Enter the first number: "))
        n2 = int(input("Enter the second number: "))
        result = n1/n2
        print(n1, "/", n2, "=", result)

    elif option == "5":
         print("Thank you for using the app")
         break