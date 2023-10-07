def is_password_valid(some_password):
    errors_in_password = []
    counter = 0
    if len(some_password) < 6 or len(some_password) > 10:
        errors_in_password.append("Password must be between 6 and 10 characters")
    if not some_password.isalnum():
        errors_in_password.append("Password must consist only of letters and digits")
    for character in some_password:
        if character.isdigit():
            counter += 1
    if counter < 2:
        errors_in_password.append("Password must have at least 2 digits")
    return errors_in_password


password = input()
list_of_errors = is_password_valid(password)

if len(list_of_errors) == 0:
    print("Password is valid")
else:
    print("\n".join(list_of_errors))