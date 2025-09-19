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
        ttaxes = float(input("Please provide the employee's taxes "))

        nnetPay = bbasicPay + aallowance
        ggrossPay = nnetPay - ttaxes - ddeductions

        myEmployees.update({eid: {
            "Name": nname,
            "Basicpay": bbasicPay,
            "Allowance": aallowance,
            "Deductions": ddeductions,
            "Taxes": ttaxes,
            "Net Pay": nnetPay,
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
                 Name = input("Please provide the employee's name: ")
                 BasicPay = input("Please provide the employee's basic pay: ")
                 Allowance = input("Please provide the employee's allowance: ")
                 Deductions = input("Please provide the employee's deductions: ")
                 Taxes = float(input("Please provide the employee's taxes "))

                 NetPay = BasicPay + Allowance
                 GrossPay = NetPay - (Taxes + Deductions)

            myEmployees[employee1].update({
                    "name": Name,
                    "Basic pay": BasicPay,
                    "Allowance": Allowance,
                    "Deductions": Deductions,
                    "Taxes": Taxes,
                    "Net Pay": NetPay,
                    "Gross Pay": GrossPay,
                })



    elif option == "4":
        for employees_record in myEmployees.items():
             print("These are all the employees in the record", employees_record)
             print("------------------------------------")

    elif option == "5":
        print("Thank you for using this program!")
        break


