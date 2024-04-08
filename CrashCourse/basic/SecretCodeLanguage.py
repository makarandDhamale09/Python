import random
import string


def get_random_letter_string(n):
    strList = random.choices(string.digits + string.ascii_lowercase + string.ascii_uppercase, k=n)
    strEmpty = ""
    return strEmpty.join(strList)


def decode_word(word):
    updatedWord = word[3:-3]
    return updatedWord[-1:] + updatedWord[:-1]


def move_first_letter_to_back(word):
    return word[1:] + word[0]


def reverse_string(word):
    return word[::-1]


def encode(message):
    """This Method Encode the message in a secret code. The encode message can be decoded using the method DECODE in
    this class"""
    splitMessage = message.split(" ")
    encodedMessage = " "
    for i in splitMessage:
        if len(i) > 3:
            encodedMessage = encodedMessage + " " + get_random_letter_string(3) + move_first_letter_to_back(
                i) + get_random_letter_string(3)
        else:
            encodedMessage = encodedMessage + " " + reverse_string(i)
    return encodedMessage.strip()


def decode(message):
    """It decodes the message encoded by the ENCODE Method in this class"""
    splitMessage = message.split(" ")
    decodedMessage = " "
    for i in splitMessage:
        if len(i) > 3:
            decodedMessage = decodedMessage + " " + decode_word(i)
        else:
            decodedMessage = decodedMessage + " " + reverse_string(i)
    return decodedMessage.strip()


msg = input("Enter your message : \n")
func = int(input("What you want to do \n1. Encode \t 2. Decode \n"))

if func == 1:
    msg = encode(msg)
else:
    msg = decode(msg)

print(f"The message is : '{msg}'")
