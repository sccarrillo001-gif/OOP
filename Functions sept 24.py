def area_rectangle():
    l = int(input("Enter length"))
    b = int(input("Enter breadth"))
    print("The area is:", l * b)

def area_cube():
    l = int(input("Enter length"))
    b = int(input("Enter breadth"))
    h = int(input("Enter height"))
    print("The area is:", l * b * h)

def area_circle():
    r = int(input("Enter the radius"))
    print("The area is:", 3.14 * r * r)

def circumference_circle():
    r = int(input("Enter the radius"))
    print("The area is:", 3.14 * r * 2)

def volume_sphere():
    r = int(input("Enter the radius"))
    print("The area is:", (4/3) * 3.14 * r * r * r)


#Main code-----------------------------
while 1:
    print("Please choose one of the following: ")
    print("1. Area of a rectangle")
    print("2. Area of a cube")
    print("3. Area of a circle")
    print("4. Circumference of a circle")
    print("5. Volume of a Sphere")
    print("6. Quit Application")

    option = input("Please enter your choice here: ")

    if option == "1":
        area_rectangle()

    elif option == "2":
        area_cube()

    elif option == "3":
        area_circle()

    elif option == "4":
        circumference_circle()

    elif option == "5":
        volume_sphere()

    elif option == "5":
        print("Thank you for using this program!")
        break

#QUEUE--FIFO (First in/First out)
#STACK--





