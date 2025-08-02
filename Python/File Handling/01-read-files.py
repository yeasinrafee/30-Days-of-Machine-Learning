# f = open("demofile.txt")
# print(f.read())

# with open("demofile.txt") as f:
#     print(f.read())

# Reading Lines
# print(f.readline())

# Close File:
# f.close()

# Writing on a file
# with open("demo.txt", "a") as f:
#     f.write("Now the file has more content!")
    
# with open("demofile.txt") as f:
#     print(f.read())
    
# Overwrite Existing Content: 
# "w" - Write - will create a file if the specified file does not exists
# with open("demofile.txt", "w") as f:
#     f.write("Woops! I have deleted the content!")
# with open("demofile.txt") as f:
#     print(f.read())
    
# To create a new file in Python, use the open() method, with one of the following parameters:
# "x" - Create - will create a file, returns an error if the file exists
# f = open("myfile.txt", "x")

# "a" - Append - will create a file if the specified file does not exists
# with open("myfile.txt", "a") as f:
#     f.write("I am writing on the file")
    
# with open("myfile.txt") as f:
#     print(f.read())

# Deleting a file
import os
os.remove("./demofile.txt")

# Deleting a Folder:
import os
os.rmdir("myfolder")        # It will remove only the empty folders