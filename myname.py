MIN_LENGTH = 8
while True:
    password = input("Please enter a password: ")
    # Check if the password meets the minimum length requirement
    if len(password) >= MIN_LENGTH:
        break
    else:
        print("Password must be at least {} characters long.".format(MIN_LENGTH))

print("*" * len(password))
