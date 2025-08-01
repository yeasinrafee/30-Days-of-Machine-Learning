fruits = ["Apple", "Banana", "Cherry"]
for x in fruits:
    print(x)
    
# Looping through a string 
for x in "Banana":
    print(x)
    
# Using break statement
for x in fruits:
    print(x)
    if x == "Banana":
        break 
    
# The range() function
for x in range(6):
    print(x)
    
for x in range(2, 6):
    print(x)
    
for x in range(10, 100, 10):        # Third parameter is for increment
    print(x)
    
# Else in for loop
for x in range(6):
    print(x)
else:
    print("Done")
    
# Nested for Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)