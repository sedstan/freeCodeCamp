import re
import secrets
import string


def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
    """Generates a password
        :params: length: number - the length of characters to use
        :params: nums: number - the amount of numbers to use
        :params: special_chars: number - the amount of special characters to use
        :params: uppercase: number - the number of uppercase characters to use
        :params: lowercase: number - the number of lowercase characters to use
        :return string - the new, generated password"""
    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    while True:
        password = ''
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)
        
        constraints = [
            (nums, r'\d'),
            (special_chars, fr'[{symbols}]'),
            (uppercase, r'[A-Z]'),
            (lowercase, r'[a-z]')
        ]

        # Check constraints        
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break
    
    return password
    
if __name__ == '__main__':
    new_password = generate_password()
    print('Generated password:', new_password)
