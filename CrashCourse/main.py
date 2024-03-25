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
tup = ("Makarand", "abc", "apple", "banana")
dictonary = {"name": "Makarand", "age": 31, "canVote": True}

print(type(a))
print(type(b))
print(type(c))
print(type(lists))
print(type(tup))
print(type(dictonary))

print(lists)
print(tup)
print(dictonary)

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
    if i == "a":
        print("This is a special character 'a' ")

# Range in loop
for k in range(5):
    print(k)

# Functions in python
print("---------Functions------------")


def calculate_gmean(num1, num2):
    mean = (num1 * num2) / (num1 + num2)
    print(mean)
    return mean


calculate_gmean(7, 8)
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


# Write fibonacci series using recurssion
def fibonacci(n):
    """Calculates Fibonacci series till number n"""
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(9))

# Sets
print("-------------Sets---------------")
# defining sets we use curly braces {}
sets = {1, 2, 3, 3, 3, 4}
print(sets)
s1 = {1, 2, 3, 6}
s2 = {4, 5, 6}
s3 = s1.union(s2)  # union creates a new set
print(s3)
print(s1, s2)
s1.update(s2)  # update method used to update same method
print(s1)

cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities__intersection = cities1.intersection(cities2)  # creates an intersection of two sets
print(cities__intersection)
cities1.intersection_update(cities2)  # will add all intersection values to the set on which the operation is being
# performed

# Dictionary ####
print("----------Dictionary--------")
dic = {
    "Makarand": "Human being",
    "Spoon": "Object"
}
print(dic["Makarand"])
print(dic.keys())

# Iterating the key and values
for key in dic.keys():
    print(dic[key])

print(dic.values())
print(dic.items())

# Exception Handling in Python
print("------Exception handling---------")
# Write a program to print the table of number
# num = input("For Which number the table should be Printed : ")
num = 5
try:
    for i in range(1, 11):
        print(f"{int(num)} X {int(i)} = {int(num) * int(i)}")
except ValueError as e:
    print(f"Invalid Number value '{num}'")
finally:
    print("This is finally code...")

# We want that this line should be executed no matter what
print("Some Imp lines of code")

# Custom Errors
# a = int(input("Enter value between 5 and 9 : "))
a = 7
if a < 5 or a > 9:
    raise ValueError("Value should be between 5 and 9")
