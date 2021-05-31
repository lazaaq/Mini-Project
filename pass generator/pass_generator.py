# selesai
import random as rd
import string


def pass_generator():
    character = list(string.ascii_lowercase +
                     string.ascii_uppercase + string.digits)
    random_length = rd.randint(10, 15)
    s = ""
    for i in range(random_length):
        s += rd.choice(character)
    return s


myPass = pass_generator()
print(myPass)
