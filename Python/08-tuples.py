mytuple = ("Apple", "Banana", "cherry")

print(mytuple)
print(len(mytuple))
print(type(mytuple))

tuple1 = ("abc", 34, True, 90, "male")
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)
print(tuple1)

# Accessing a Tuple: 
print(thistuple[1])
print(thistuple[-1])
print(tuple1[1:4])
print(thistuple[:1])
print(thistuple[1:])
print(tuple1[-4:-1])


# Updating a Tuple 
#  1. Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
#  2. We can convert the tuple into a list, change the list, and convert the list back into a tuple.

x = ("Yeasin", "Arefin", "Rafee")
y = list(x)
y[1] = "Arafat"
# Appending 
y.append("Arefin")
x = tuple(y)
print(x)

tup1 = ("Pen", "Pencil", "Eraser")
tup2 = ("Notebook",)
tup1 += tup2
print(tup1)

# Removing Tuple 
z = list(tup1)
z.remove("Pen")
tup1 = tuple(z)
print(tup1)


# Unpacking Tuple 
colors = ("Red", "Green", "Yellow", "Black", "White")
# (car, tree, sun, tv, board) = colors
# print(car)
# print(tree)
# print(board)

(car, tree, *tv) = colors
print(car)
print(tree)
print(tv)


# Method	Description
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found