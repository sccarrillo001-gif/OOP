# Class Exercise 1-----------------------------------------------------------

'''
file1 = open("test1.txt", "w")       # also with open("student.dat", "wb") as file1:
file1.writeline("Hello World! \n")
file1.writeline("Bye! \n")

file1.close()

file2 = open("test1.txt", "r")

for line in file2:
    print(line)

file2.close()
'''

#MODES: read only, write only, append

# Class Exercise 3-----------------------------------------------------------

import pickle
'''
d = {"stu1": {"Name": "John", "Age": "21", "Id": 28},
    "stu2": {"Name": "John", "Age": "99", "Id": 29},
    "stu3": {"Name": "Js", "Age": "70", "Id": 30},
     }


with open("students.dat", "wb") as file1:
    pickle.dump(d, file1)
file1.close()

with open("students.dat", "rb") as file2:
    mydictionary = pickle.load(file2)

print(mydictionary)
file2.close()
'''

# Class Exercise 3-----------------------------------------------------------
d = {"stu1": {"Name": "John", "Age": "21", "Id": 28},
    "stu2": {"Name": "John", "Age": "99", "Id": 29},
    "stu3": {"Name": "Js", "Age": "70", "Id": 30},
     }

import pickle

with open("students.dat", "rb") as file2:
    mydictionary = pickle.load(file2)
file2.close()

print(mydictionary["stu1"]["Name"])
print(mydictionary["stu1"]["Age"])

i=1
for x in mydictionary:
    var = "stu"+str(i)
    print(mydictionary[var]["Name"])
    i+=1

# Class Exercise 4-----------------------------------------------------------
d = {"usr1": {"uid": "John", "Age": "21", "Id": 28},
    "usr2": {"uid": "John", "Age": "99", "Id": 29},
    "usr3": {"uid": "Js", "Age": "70", "Id": 30},
     }