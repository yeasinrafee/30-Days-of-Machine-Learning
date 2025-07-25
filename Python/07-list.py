# Lists are used to store multiple items in a single variable.

mylist = ["Yeasin", "Arefin", "Rafee"]
print(mylist)

# Rules:
#  1. List items are ordered, changeable, and allow duplicate values.
#  2. Ordered means that the items have a defined order, and that order will not change.
#  3. Adding new items to a list, the new items will be placed at the end of the list.
#  4. The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

print(len(mylist))
print(type(mylist))


# It is also possible to use the list() constructor when creating a new list.
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

# Accessing list items
print(thislist[1])      # // Access From First
print(thislist[-1])     # // Access From Last
print(thislist[2:5])    # // Return List from middle
print(thislist[:5])    # // Return List from first to given number
print(thislist[2:])    # // Return List from given number to last

# Change List Item
thislist[1] = "pineapple"
thislist[2:3] = ["watermelon"]
thislist.insert(1, "cherry")
print(thislist) 

# Add List Items
thislist.append("orange")
thislist.extend(mylist)
print(thislist)

# Removing List Items 
thislist.remove("cherry")
thislist.pop(1)     # Will remove the specified index item
thislist.pop()      # Will remove the last item
del thislist[0]     # Will remove the indexed item
# del thislist      # Will remove the list completely
# thislist.clear()  # Will clear the whole list
print(thislist)