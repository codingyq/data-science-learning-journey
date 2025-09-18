# creating student data type. We can define attribute about a student - modeling a student. Use basic data type like strings, numbers, booleans to map out want a student should be and should have
class Student:
    def __init__(self, name, major, gpa, is_on_probation): # initialize function
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

# When we create a student (the Object), we are actully calling this initialize function: def __init__(self, name, major, gpa, is_on_probation):
  # In def function: when we pass the name, major, the GPA, those values are actually getting stored over def function, and they are just parameters
  # In      self.name = name           ----  Assigning values.
  #         self.major = major
  #         self.gpa (the student object's gpa) = gpa (the GPA we passed in)
  #         self.is_on_probation = is_on_probation,
  # We assign them to the actual attributes of the object. "ok, the name of the student object(self.name) is going to be equal to the name(name) that we passed in"
  # self --- refer to the actual object