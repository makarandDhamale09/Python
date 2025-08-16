#List
""""
Lists are mutable sequences in Python, meaning they can be modified after creation.
They are defined using square brackets and can contain mixed data types.
Lists support various operations such as appending, removing, and inserting elements.
Lists can also be iterated over using loops.
"""

print("Lists: \n------------------------------")
list = ["Apple", "Banana", "Cherry", "Date", "Elderberry", 3]

# for item in list:
#   print(item)

list.append("Fig")
list.remove("Banana")
list.insert(2, "Grape")

print(f"Length of list is {list.__len__()}")

for index, item in enumerate(list):
  print(f"Item {index}: {item}")


# Tuples
"""
Tuples are immutable sequences in Python, meaning once created, they cannot be modified.
They are defined using parentheses and can contain mixed data types.
"""
print("\nTuples:\n--------------------------------")
tuple = ("Apple", "Banana", "Cherry", "Date", "Elderberry", 3)

# tuple.append("Fig")  # This will raise an AttributeError since tuples are immutable

count = tuple.count("Apple")  # Count occurrences of "Apple"
print(f"Count of 'Apple': {count}")

for item in tuple:
  print(item)



# Dictionaries
"""
Dictionaries are mutable mappings in Python, consisting of key-value pairs.
They are defined using curly braces and can contain mixed data types.
Dictionaries allow for fast lookups, insertions, and deletions based on keys.
These are similar to hash maps in other programming languages.
"""

print("\nDictionaries:\n--------------------------------")
dictionary = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "is_student": False,
    "courses": ["Math", "Science", "History"]
}

# Accessing values by keys
print(f"Name: {dictionary['name']}")
print(f"Age: {dictionary['age']}")
print(f"City: {dictionary['city']}")  


# Sets
"""
Sets are unordered collections of unique elements in Python.
They are defined using curly braces or the set() constructor.
Sets support operations like union, intersection, and difference.
Sets are useful for membership testing and eliminating duplicate entries.
"""
print("\nSets:\n--------------------------------")
colors = {"red", "green", "blue"}

colors.add("yellow")  # Adding an element
colors.remove("green")  # Removing an element
colors.update(["purple", "orange"])  # Adding multiple elements
print(f"Colors set: {colors}")