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

#