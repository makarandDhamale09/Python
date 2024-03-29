import os

print(f"Path {os.getcwd()}")

currentDir = os.getcwd()
name = "data"
fullPath = os.path.join(currentDir, name)
print(fullPath)

# Create the data dir only if it does not exist
if not os.path.exists(fullPath):
    os.mkdir(fullPath)

filePath = os.path.join(fullPath, "myFile.txt")
print(filePath)

# Create a file only if it does not exist
if not os.path.exists(filePath):
    with open(filePath, "w") as file:
        file.write("This is the content of this file\n")

f = open(filePath, "r")
print(f.read())
f.close()

print("------")
# 'with open' it is not required to close the file
with open(filePath, "w") as file:
    file.write('This is the second line\n')
    file.write("This is the third line\n")

with open(filePath, "r") as file:
    read_lines = file.readlines()
    for line in read_lines:
        print(f"line is : {line}")

# Some other methods like seek and tell
print(type(file))
with open(filePath, "r") as f:
    # move to the 10th charater in file
    f.seek(10)
    # read 10 characters from 10th character
    data = f.read(10)
    print(data)
    # tell function tells where the file pointer is currently
    print(f.tell())

# truncate will reduce the file to number of character specified
with open(filePath, "a") as f:
    f.truncate(5)
