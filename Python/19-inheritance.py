class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

# class Student(Person):
#     def __init__(self, fname, lname):
#         Person.__init__(self, fname, lname)

# Using the Super function
# Python also has a super() function that will make the child class inherit all the methods and properties from its parent
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
    def welcome(self):
        print(f"Welcome, Mr. {self.fname} {self.lname}")
        
x = Student("Yeasin", "Rafee", 2025)
print(x.fname)
print(x.lname)
print(x.graduationyear)
x.welcome()

