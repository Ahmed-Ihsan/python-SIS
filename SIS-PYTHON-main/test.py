import string
import random



def password_generator(length=8):

    LETTERS = string.ascii_letters
    NUMBERS = string.digits
    # create alphanumerical from string constants
    printable = f'{LETTERS}{NUMBERS}'

    # convert printable from string to list and shuffle
    printable = list(printable)
    random.shuffle(printable)

    # generate random password and convert to string
    random_password = random.choices(printable, k=length)
    random_password = ''.join(random_password)
    return random_password

a = password_generator()
print(a)