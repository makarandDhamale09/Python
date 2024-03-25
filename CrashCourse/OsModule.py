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
        file.write("This is the content of this file")

f = open(filePath, "r")
print(f.read())
f.close()
