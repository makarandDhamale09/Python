# def double(x):
#     return x * 2

double = lambda x: x * 2

print(double(5))


# passing lambda function as a parameter to a method
def appl(fx, value):
    return 6 + fx(value)


# print(appl(lambda x: x * 2, 3))
print(appl(double, 3))
