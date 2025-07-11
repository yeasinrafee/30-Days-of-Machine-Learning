# There are three numeric types in Python:
# 1. int
# 2. float
# 3. complex    (Complex numbers are written with a "j" as the imaginary)

x = 10
y = 34.56
z = 1j + 3

print(type(x))
print(type(y))
print(type(z))

a = 56e8
print(a)

# Type Conversion or casting
b = float(x)
c = int(y)
d = complex(x)
print(b)
print(c)
print(d)

# Random Number
import random
print(random.randrange(1, 10))