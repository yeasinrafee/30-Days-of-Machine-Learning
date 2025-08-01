# In python function is defined using the def keyword:
def my_function():
    print("Hello world")  
my_function()

def full_name(fName, lName):
    print(f"My name is {fName} {lName}")
full_name("Yeasin", "Rafee")

# Arbitrary Arguments, *args
# If the number of arguments is unknown, add a * before the parameter name
def my_func(*kids):
    print(f"The youngest child is {kids[2]}")
my_func("Yeasin", "Arefin", "Rafee")

# If the number of keyword arguments is unknown, add a double ** before the parameter name
def my_func2(**kid):
    print(f"His last name is {kid["lname"]}")
my_func2(fname = "Yeasin", lname = "Rafee")

# Default Parameter
def my_func3(country = "Bangladesh"):
    print(f"I am from {country}")
my_func3()

# Passing a List as an Argument
def my_func4(food):
    for x in food:
        print(x)
fruits = ["apple", "banana", "mango"]
my_func4(fruits)

# Return values
def my_func5(x):
    return 5 + x
print(my_func5(5))

# Positional Only Argument:
def my_func6(x, /):
    print(x)
my_func6(3)

# Keyword Only Argument:
def my_func7(*, x):
    print(x)
my_func7(x = 5)

# Combine Positional-Only and Keyword-Only
def my_func8(a, b, /, *, c, d):
    print(a + b + c + d)
my_func8(5, 6, c = 7, d = 8)

# Recursive Function
def my_func9(x):
    if x == 0:
        return
    my_func9(x - 1)
    print(x)
my_func9(5)