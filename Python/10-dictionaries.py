thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "colors": ["red", "white", "blue"]
}

# Rules: 
# 1. Dictionaries are used to store data values in key:value pairs.
# 2. A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# 3. As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# 4. Dictionaries are written with curly brackets, and have keys and values.id
# 5. Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
# 6. Dictionaries cannot have two items with the same

print(thisdict)
print(thisdict["brand"])
print(len(thisdict))
print(type(thisdict))

thisdict2 = dict(name = "Yeasin", age = 24, country = "Bangladesh")
print(thisdict2)

# ** Accessing Items 
x = thisdict["model"]
x = thisdict.get("model")
y = thisdict.keys()         # The keys() method will return a list of all the keys in the dictionary.
z = thisdict.values()       # The values() method will return a list of all the values in the dictionary.
q = thisdict.items()        # The items() method will return each item in a dictionary, as tuples in a list.

print(y, z, q)


# * Change values 
thisdict["year"] = 2018
thisdict.update({"year": 2020})
print(thisdict)

# * Removing Items: 
thisdict2.pop("country")        # The pop() method removes the item with the specified key name
thisdict2.popitem()     #The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead)
del thisdict2["name"]       # The del keyword removes the item with the specified key name
thisdict2.clear()        # The clear() method empties the dictionary
print(thisdict2)

# * Copy Dictionary
thisdict2 = thisdict.copy()
thisdict2 = dict(thisdict)
print(thisdict2)