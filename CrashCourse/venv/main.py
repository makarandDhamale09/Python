# hello
print("The \t line above is a \n comment")

'''This is a multiline comment
second line
third line'''

# printing with a seperator and end
# Default seperator is 'space'
# Default end is 'newline'
print("Hey", 7, 6, sep="~", end="007\n")
print("Hey", 6, 7)

# Variables
print("--------Variables---------")
a = 1
b = "Makarand"
c = True
list = [8, 2.3, [-4, 5], ["apple", "banana"]]
tuple = ("Makarand", "abc", "apple", "banana")
dict = {"name" : "Makarand", "age": 31, "canVote" : True}

print(type(a))
print(type(b))
print(type(c))
print(type(list))
print(type(tuple))
print(type(dict))

print(list)
print(tuple)
print(dict)

# Input in python
# print("-----------Input----------")
# a = input()
# print("The input Entered is", a)
# a = input("Enter your input : ")
# print("My name is", a)

# Looping through the string
print("Looping through the string")
name = "Makarand"
print(name[0])

for character in name:
    print(character)

for i in enumerate(name):
    print(i)