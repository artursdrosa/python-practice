import random
import string

def create_safe_password():
    uppercase = list(string.ascii_uppercase)
    lowercase = list(string.ascii_lowercase)
    digits = list(string.digits)
    special = list(string.punctuation)

    password = [random.choice(uppercase), random.choice(lowercase), random.choice(digits), random.choice(special)]

    characters = uppercase + lowercase + digits + special

    try:
        length = int(input("Enter the length of the password: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        exit()

    return ''.join(password) + ''.join(random.choice(characters) for i in range(length - 4))