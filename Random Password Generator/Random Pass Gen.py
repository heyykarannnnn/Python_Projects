import random
import string

while True:
    def generate_password(length):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

    password_length = int(input("Enter the length of the password: "))
    random_password = generate_password(password_length)
    print("Random Password:", random_password)
