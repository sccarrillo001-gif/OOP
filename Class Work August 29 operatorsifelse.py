
course1 = int(input("Enter the grade for course1: "))
course2 = int(input("Enter the grade for course2: "))
course3 = int(input("Enter the grade for course3: "))
course4 = int(input("Enter the grade for course4: "))
course5 = int(input("Enter the grade for course5: "))

total = course1 + course2 + course3 + course4 + course5
total_percentage = ((total/500)*100)

if total_percentage <= 100 and total_percentage >= 90:
    print ("Grade A")

elif total_percentage < 90 and total_percentage >= 80:
    print("Grade B")

elif total_percentage < 80 and total_percentage >= 70:
    print("Grade C")

elif total_percentage < 70 and total_percentage >= 60:
    print("Grade D")

elif total_percentage < 60:
    print("Grade F")