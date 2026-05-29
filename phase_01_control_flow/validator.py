print ("Welcome to the Validator program!")

password = input("Please enter your password: ")

error = []

if len(password) < 8:
    error.append("Password must be at least 8 characters long.")