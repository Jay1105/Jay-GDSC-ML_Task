import random
import string

def generate_password(length = 10):
    upper_char = string.ascii_uppercase
    lower_char = string.ascii_lowercase
    pun = string.punctuation
    digit = string.digits

    characters = upper_char + lower_char + digit + pun

    password = ''

    if length >= 4:
        password += random.choice(upper_char)
        password += random.choice(lower_char)
        password += random.choice(digit)
        password += random.choice(pun)

        length -= 4
        for i in range(length):
            password += random.choice(characters)
    else:
        for i in range(length):
            password += random.choice(characters)
    
    return password

tp = generate_password(15)
print(tp)