# **Defining Sets 
myset = {"apple", "banana", "cherry"}
set1 = {"abc", 24, True, 40, "male"}
thisset = set(("Yeasin", "Arefin", "Rafee"))

print(myset)
print(len(myset))
print(type(myset))

# Rules: 
# 1. Sets are used to store multiple items in a single variable.
# 2. A set is a collection which is unordered, unchangeable*, and unindexed, also it do not allow duplicate values.
# 3. Set items are unchangeable, but we can remove items and add new items.
# 4. Sets are written with curly brackets.
# 5. The values True and 1 are considered the same value in sets, and are treated as duplicates
# 6. The values False and 0 are considered the same value in sets, and are treated as duplicates

# *Access Set items 
for x in thisset:
    print(x)

print(24 in set1)
print(24 not in set1)

# *Add Set Items:
thisset.add("HongaPonga")
print(thisset)

myset.update(set1)
print(myset)


# *Remove Set items:

thisset.remove("Rafee")
print(thisset)
# If the item to remove does not exist, remove() will raise an error.

thisset.discard("HongaPonga")
print(thisset)
# If the item to remove does not exist, discard() will NOT raise an error

x = set1.pop()
print(x)
print(set1)

# thisset.clear()       # This will empties the set
# del this              # This will delete the set completely
