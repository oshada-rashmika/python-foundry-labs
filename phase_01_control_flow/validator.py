print ("Welcome to the Validator program!")

password = input("Please enter your password: ")

error = []

if len(password) < 8:
    error.append("Password must be at least 8 characters long.")

has_number = False

for char in password:
    if char.isdigit():
        has_number = True
        break
if not has_number:
    error.append("Password must contain at least one number.")

special_characters = "!@#$%^&*()-_=+[]{}|;:',.<>?/"
has_special = False

for char in password:
    if char in special_characters:
        has_special = True
        break
if not has_special:
    error.append("Password must contain at least one special character.")

if len(error) == 0:
    print("Password is valid!")
else:
    print("Password is invalid:")
    for err in error:
        print(f"- {err}")