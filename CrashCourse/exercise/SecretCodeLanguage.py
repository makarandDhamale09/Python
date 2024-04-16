import random
import string


def get_random_letter_string(n):
    str_list = random.choices(string.digits + string.ascii_lowercase + string.ascii_uppercase, k=n)
    str_empty = ""
    return str_empty.join(str_list)


def decode_word(word):
    updated_word = word[3:-3]
    return updated_word[-1:] + updated_word[:-1]


def move_first_letter_to_back(word):
    return word[1:] + word[0]


def reverse_string(word):
    return word[::-1]


def encode(message):
    """This Method Encode the message in a secret code. The encode message can be decoded using the method DECODE in
    this class"""
    split_message = message.split(" ")
    encoded_message = " "
    for i in split_message:
        if len(i) > 3:
            encoded_message = encoded_message + " " + get_random_letter_string(3) + move_first_letter_to_back(
                i) + get_random_letter_string(3)
        else:
            encoded_message = encoded_message + " " + reverse_string(i)
    return encoded_message.strip()


def decode(message):
    """It decodes the message encoded by the ENCODE Method in this class"""
    split_message = message.split(" ")
    decoded_message = " "
    for i in split_message:
        if len(i) > 3:
            decoded_message = decoded_message + " " + decode_word(i)
        else:
            decoded_message = decoded_message + " " + reverse_string(i)
    return decoded_message.strip()


msg = input("Enter your message : \n")
func = int(input("What you want to do \n1. Encode \t 2. Decode \n"))

if func == 1:
    msg = encode(msg)
else:
    msg = decode(msg)

print(f"The message is : '{msg}'")
