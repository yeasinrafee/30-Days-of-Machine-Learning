age = 19

if age < 18:
    print("You can not drive drive!!")
elif age > 65:
    print("You can drive with other person!!")
else:
    print("You can drive....")
    
a = 34
b = 87
c = 53

if a > b and a > c:
    print("A is greater..!")
elif b > c:
    print("B is greater..!")
else:
    print("C is greater..!")
    
if a > b or a > c:
    print("A is middle number.")
    
print("A is greater.") if a > b else print("B is greater.")

if b > a:
    pass

if not a > b:
    print("A is not greater than B.")