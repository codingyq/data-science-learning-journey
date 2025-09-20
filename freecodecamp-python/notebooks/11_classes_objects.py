# Classes and Objects make python more organized and powerful.
# Class is the template for the xx and define what a xxx is - like an overview of what the xx data type is.
# An object is the actual xx. - it just an instance of a class.


# Class: define our own data type - like hey here's another data type that we want to use in python.
  # Basic data type: strings like plain text, numbers, boolean values -  3 main types of data we are going to be working with in python.
  # All sorts of structures we can use to store that data: list, dictionaries.
  #  When we want to represent somthing but the data types we have available to us in python can't cover that:
  #  We can create our own data types. e.g. we create a PHONE data types and store all information we know about the phone inside that data type.
  #  In python, we could create a class for it. IT'S LIKE AN OVERALL TEMPLATE, it defines what a xx is.

# Case: We are writing a program and want to represent a student inside of this program. - writing program for university and want to model a student.
# Classes defines the student data type and the object is the actual students
   #  1. Create a student class: (1) create a new python file in the folder and named it "Student"
   #                             (2) State the class & Make initialize function that define the attributes that can describe the students
   #                             (3) Finish it by making variables that will be involved
   #  2. Use the student class:  (1) from XX import XX
   #                             (2) define object


# Objects:
    # (Remember: class - an overall template. It defines what a Student is; Object is an actual student with actual information)
from student import Student # from the student FILE import the student CLASS - same Student. but refers differently

student1 = Student("Jim", "Business",3.1, False) # saying I want to create a student object

    # Once we create the student object, we can access the information about the student
print(student1.name)
print(student1.gpa)

student2 = Student("Pam", "Art",2.5, True)
print(student2.gpa)


# To sum up what We've did in 11 Classes & Objects + student.py:
    # we created a student data type and we created student objects, and now we're able to represent a student inside our program
