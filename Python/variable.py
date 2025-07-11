x = 5
name = "Rafee"
print(x)
print(name)
print(type(x))
print(type(name))

# Rules for Python variables:
# 1. A variable name must start with a letter or the underscore character
# 2. A variable name cannot start with a number
# 3. A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# 4. Variable names are case-sensitive (age, Age and AGE are three different variables)
# 5. A variable name cannot be any of the Python keywords.

# Multi Words Variable Names
# 1. Camel Case:
myName = "Rafee"
# 2. Pascal Case: 
MyName = "Rafee"
# 3. Snake Case:
my_name = "Rafee"

# Many Values to Multiple Variables
x, y, z = 5, 6, 7
print(x)
print(y)
print(z)

# One value to Multiple Variables
a = b = c = 10
print(a, b, c)

# Output of variables:
firstName = "Yeasin"
lastName = "Rafee"
print(firstName + " " + lastName)

# Global Variables
def myfunc():
    global x
    x = 10
    print("Inside func: ", x)
myfunc()

print("Outside func: ", x)
