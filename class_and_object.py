import PIL

class ExampleClass:
    example_variable = 10

an_obect = ExampleClass()
print(an_obect.example_variable)

class Student:
    def __init__(self, name, id, cgpa):
        self.name = name
        self. id = id
        self.cgpa = cgpa

    def a_function(self):
        print("The name is ", self.name)
a_student = Student("Md Tarikul Islam Suzan", 12456789, 3.5)
a_student.a_function()