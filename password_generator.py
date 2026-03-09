import random
import string

print("===== PASSWORD GENERATOR =====")

# Ask user for password length
length = int(input("Enter the desired password length: "))

# Character combinations
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

all_characters = letters + digits + symbols

# Generate password
password = ""
for i in range(length):
    password += random.choice(all_characters)

# Display password
print("Generated Password:", password)