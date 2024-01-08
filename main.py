import random
import string


def generate_password():
    length = int(input("Enter the desired length of the password: "))

    include_letters = input("Include letters? (yes/no): ").lower() == 'yes'
    include_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
    include_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'
    external_symbols = input("Include additional special characters? (yes/no): ").lower() == 'yes'

    characters = ''

    if include_letters:
        characters += string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation
    if external_symbols:
        external_chars = '!@#$%^&*()_-+=<>?'
        characters += external_chars

    if not characters:
        raise ValueError("At least one character set must be included.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


# Example usage:
password = generate_password()
print(password)