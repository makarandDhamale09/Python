import json
import datetime

x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}


y = json.dumps(x)

print(y)
print(type(y))
print(type(x))
print(x["name"])

thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)


date = datetime.datetime.now()
print(date)

print(date.year)
print(date.month)
print(date.day)
print(date.hour)
print(date.minute)
print(date.second)
print(date.strftime("%Y-%m-%d %H:%M:%S"))

