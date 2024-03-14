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
lists = [8, 2.3, [-4, 5], ["apple", "banana"]]
tuple = ("Makarand", "abc", "apple", "banana")
dict = {"name": "Makarand", "age": 31, "canVote": True}

print(type(a))
print(type(b))
print(type(c))
print(type(lists))
print(type(tuple))
print(type(dict))

print(lists)
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

# String methods
print("---------Strings---------------")
a = "Makarand1"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.center(50))
print(a.count("a"))
print(a.isalpha())
print(a.isalnum())
print(a.islower())
print(a.swapcase())

# MatchCase is like the switch case
print("-------Match case--------")
x = 7

match x:
    case 4:
        print("This is 4")
    case 0:
        print("This is zero")
    case _:
        print("This is default case")

# For Loop
print("----------For Loop-----------")
name = "Makarand"
for i in name:
    print(i)
    if (i == "a"):
        print("This is a special character 'a' ")

# Range in loop
for k in range(5):
    print(k)

# Functions in python
print("---------Functions------------")


def calculateGmean(a, b):
    mean = (a * b) / (a + b)
    print(mean)
    return mean


calculateGmean(7, 8)
lists = [1, 2, 3, "Makarand", True]
print(lists[-2])

# Tuples are list that cannot be modified
print("---------Tuples---------- ")
tup = (1, "Makarand", 3, 4, 5, 6, True)
print(type(tup))
# slicing in tuple same as list
tup2 = tup[1:4]
print(tup2)
if 4 in tup:
    print("4 is present in this tuple")

# F-Strings : String formatting
print("-------F-Strings----------")

# old way
letter = "Hey my name is {} and I am from {}"
country = "India"
name = "Makarand"
print(letter.format(name, country))

# with f string
print(f"Hey my name is {name} and I am from {country}")
price = 49.09999
print(f"For only {price:.2f} dollars!!")

# DocString
print("--------DocStrings--------")


# DocStrings are always after the func def
def square(n):
    """Takes in a number n and returns the square of n"""
    print(n ** 2)


square(5)
print(square.__doc__)
