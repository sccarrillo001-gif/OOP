Projects = {}
mang = []
techn = []
team = []


print("Welcome!")

while True:
    print("Please choose one of the following: ")
    print("1. Project Inititation")
    print("2. Project Closure")
    print("3. Project Progress Update an employee")
    print("4. Print a specific project")
    print("4. Print all projects")
    print("5. Quit Application")

    option = input("Please enter your choice here: ")

    if option == "1":
        pid= input("Please provide the project's id: ")
        ttitle = input("Please provide the project title: ")
        mmanagers = input("Please provide the project managers: ")
        n = int("Enter how manny managers you want to enter:")
        for i in range(0,n):
            techn.append(input("Enter the managers:"))
        sstart = input("Please provide the project's start date: ")
        eend = input("Please provide the project's end date: ")
        ssponsor = input("Please provide the project's sponsor: ")
        bbudget = (input("Please provide the project's budget: "))
        n = int("Enter how manny technologies you want to enter:")
        for i in range(0,n):
            techn.append(input("Enter the technology:"))
        n = int(input("Enter how many team members you want to enter:"))
        for i in range(0, n):
            team.append(input("Enter the team member's name:"))


        Projects.update({pid:{
                            "Project_title": ttitle,
                            "managers": mmanagers,
                            "start_data": sstart,
                            "end_date": eend,
                            "sponsor": ssponsor,
                            "budget": bbudget,
                            "technologies": techn,
                            "team_members": team
    }})



    elif option == "2":
        if len(Projects) == 0:
            print("The dictionary is empty")
        else:
            project1 = input("Please provide the name of the project you want to close: ")
            if project1 not in Projects:
                print("That project is not initiated")
            else:
                del Projects[project1]

    elif option == "3":
        if len(Projects) == 0:
            print("The dictionary is empty")
        else:
            project1 = input("Please provide the id of the employee: ")
            if project1 not in Projects:
                print("That student is not in the list")
            else:
                 nname = input("Please provide the new employee's name: ")
                 bbasicPay = float(input("Please provide the new employee's basic pay: "))
                 aallowance = float(input("Please provide the new employee's allowance: "))
                 ddeductions = float(input("Please provide the new employee's deductions: "))
                 ttaxes = float(input("Please provide the new employee's taxes: "))

                 nnetPay = bbasicPay + aallowance
                 ggrosspay = nnetPay - (ttaxes + ddeductions)

            Projects[employee1].update({
                    "Name": nname,
                    "Basic Pay": bbasicPay,
                    "Allowance": aallowance,
                    "Deductions": ddeductions,
                    "Taxes": ttaxes,
                    "Net Pay": nnetpay,
                    "Gross Pay": ggrosspay,
                })


    elif option == "4":
        if len(Projects) == 0:
            print("No employees found.")

        else:
            print("These are all the employees in the record")
            for projects_record in Projects.items():
             print(projects_record)
             print("------------------------------------")

    elif option == "5":
        print("Thank you for using this program!")
        break
