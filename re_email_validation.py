import re

email = input("Enter the email address: ")

# Regular expression pattern for a valid email address
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

# Check if the email address matches the pattern
if re.match(pattern, email):
    print("Valid email address")
else:
    print("Invalid email address")
