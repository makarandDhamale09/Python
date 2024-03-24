import random
import string


def get_random_letter_string(n):
    strList = random.choices(string.digits + string.ascii_lowercase + string.ascii_uppercase, k=n)
    strEmpty = ""
    return strEmpty.join(strList)


def move_first_letter_to_back(word):
    return word[1:] + word[0]


def reverse_string(word):
    return word[::-1]


def encode(message):
    splitMessage = message.split(" ")
    encodedMessage = " "
    for i in splitMessage:
        if len(i) > 3:
            encodedMessage = encodedMessage + " " + get_random_letter_string(3) + move_first_letter_to_back(
                i) + get_random_letter_string(3)
        else:
            encodedMessage = encodedMessage + " " + reverse_string(i)
    return encodedMessage.strip()


msg = input("Enter your message : \n")
func = int(input("What you want to do \n1. Code \t 2. Decode \n"))

print(encode(msg))
