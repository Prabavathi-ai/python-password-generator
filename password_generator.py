import random
import string

print("🔐 Welcome to the Password Generator")

# Ask user for password length
length = int(input("Enter the password length: "))

# Define all possible characters
characters = string.ascii_letters + string.digits + string.punctuation

# Generate password
password = ""
for i in range(length):
    password += random.choice(characters)

# Display result
print("\n✅ Your Generated Password is:")
print(password)
