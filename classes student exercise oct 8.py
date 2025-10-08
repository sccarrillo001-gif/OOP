class Student:               #Started on oct 1 finished in oct 8
    def __init__(self):
        self.stu_id = ""
        self.stu_name = ""
        self.stu_dob = ""
        self.stu_major = ""
        self.stu_gpa = 0.0
        self.courses = []

    def add_student(self):
        self.stu_id = input("Enter the SID:")
        self.stu_name = input("Enter the name:")
        self.stu_major = input("Enter the major:")

    def edit_student(self):
        self.stu_name = input("Enter the updated name:")
        self.stu_gpa = input("Enter the updated gpa:")

    def display_student(self):
        print("StuID:", self.stu_id)
        print("StuID:", self.stu_name)
        for x in self.courses:
            print("Student courses:", x.c_name)   #From self.courses[] list

    def register_courses(self, cc1):
        self.courses.append(cc1)


class Courses:                            #properties+behavior//membervariables+memberfunctions = encapsulation
    def __init__(self):                   #abstraction: definition of classes
        self.c_id = ""
        self.c_name = ""

    def add_course(self):
        self.c_id = input("Enter the course id:")
        self.c_name = input("Enter course name:")





#Main Code

s1 = Student()
c1 = Courses()
c2 = Courses()

s1.add_student()
s1.display_student()

c1.add_course()
c2.add_course()

s1.register_courses(c1)
s1.display_student()
s1.register_courses(c2)
