print("Welcome!")

myEmployees = {}

while True:
    print("Please choose one of the following: ")
    print("1. Add an employee")
    print("2. Delete an employee")
    print("3. Modify an employee")
    print("4. Display all employees")
    print("5. Exit")

    option = input("Please enter your choice here: ")

    if option == "1":
        eid = input("Please provide the employee's id: ")
        nname = input("Please provide the employee's name: ")
        bbasicPay = float(input("Please provide the employee's basic pay: "))
        aallowance = float(input("Please provide the employee's allowance: "))
        ddeductions = float(input("Please provide the employee's deductions: "))
        ttaxes = float(input("Please provide the employee's taxes: "))

        nnetpay = bbasicPay + aallowance
        ggrossPay = nnetpay - ttaxes - ddeductions

        myEmployees.update({eid: {
            "Name": nname,
            "Basic Pay": bbasicPay,
            "Allowance": aallowance,
            "Deductions": ddeductions,
            "Taxes": ttaxes,
            "Net Pay": nnetpay,
            "Gross Pay": ggrossPay,
        }
        })

    elif option == "2":
        if len(myEmployees) == 0:
            print("The dictionary is empty")
        else:
            employee1 = input("Please provide the name of the employee you want to remove: ")
            if employee1 not in myEmployees:
                print("That employee is not in the dictionary")
            else:
                del myEmployees[employee1]

    elif option == "3":
        if len(myEmployees) == 0:
            print("The dictionary is empty")
        else:
            employee1 = input("Please provide the id of the employee: ")
            if employee1 not in myEmployees:
                print("That student is not in the list")
            else:
                 nname = input("Please provide the new employee's name: ")
                 bbasicPay = float(input("Please provide the new employee's basic pay: "))
                 aallowance = float(input("Please provide the new employee's allowance: "))
                 ddeductions = float(input("Please provide the new employee's deductions: "))
                 ttaxes = float(input("Please provide the new employee's taxes: "))

                 nnetPay = bbasicPay + aallowance
                 ggrosspay = nnetPay - (ttaxes + ddeductions)

            myEmployees[employee1].update({
                    "Name": nname,
                    "Basic Pay": bbasicPay,
                    "Allowance": aallowance,
                    "Deductions": ddeductions,
                    "Taxes": ttaxes,
                    "Net Pay": nnetpay,
                    "Gross Pay": ggrosspay,
                })


    elif option == "4":
        if len(myEmployees) == 0:
            print("No employees found.")

        else:
            print("These are all the employees in the record")
            for employees_record in myEmployees.items():
             print(employees_record)
             print("------------------------------------")

    elif option == "5":
        print("Thank you for using this program!")
        break


