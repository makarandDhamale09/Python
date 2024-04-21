def my_generator():
    for i in range(5):
        yield i


gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen)) Will throw Exception as there is no object generated
