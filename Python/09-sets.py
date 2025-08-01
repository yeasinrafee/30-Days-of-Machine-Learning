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


# ** Joining Sets
# 1. The union() and update() methods joins all items from both sets.
# 2. The intersection() method keeps ONLY the duplicates.
# 3. The difference() method keeps the items from the first set that are not in the other set(s).
# 4. The symmetric_difference() method keeps all items EXCEPT the duplicates.

set10 = {"a", "b", "c"}
set20 = {1, 2, 3}
set30 = {"Yeasin", "Arefin", "Rafee", "apple"}
set40 = {"apple", "banana", "cherry"}

# 1. Union: The union() method returns a new set with all items from both sets.
# set30 = set10.union(set20)
# set30 = set10 | set20
# set50 = set10.union(set20, set30, set40)        # Joining multiple sets
# set50 = set10 | set20 | set30 | set40

y = (1, 2, 3)
z = set10.union(y)      # Join set with tuple
print(z)

# 2. Update:
# i. The update() method inserts all items from one set into another.
# ii. The update() changes the original set, and does not return a new set.
set10.update(set20)
print(set10)

# 3. Intersection: 
# i. Keep ONLY the duplicates
# ii. The intersection() method will return a new set, that only contains the items that are present in both sets.
set50 = set30.intersection(set40)
set50 = set30 & set40

# The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
# set40.intersection_update(set40)
print(set50)

# 3. Difference: 
# i. The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
set60 = set30.difference(set40)
set60 = set30 - set40
# set30.difference_update(set40)
# The difference_update() method will also keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.
print(set60)

# 4. Symmetric Differences
# i. The symmetric_difference() method will keep only the elements that are NOT present in both sets.
set70 = set30.symmetric_difference(set40)
set70 = set30 ^ set40
# set30.symmetric_difference_update(set40)
# The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set.
print(set30)