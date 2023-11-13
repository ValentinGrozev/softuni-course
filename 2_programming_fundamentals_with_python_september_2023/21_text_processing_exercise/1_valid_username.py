def valid_username(name_of_current_user):
    if valid_length(name_of_current_user) and valid_contain(name_of_current_user) \
            and no_redundant_symbols(name_of_current_user):
        return True
    return False


def valid_length(name_of_current_user):
    if 3 <= len(name_of_current_user) <= 16:
        return True
    return False


def valid_contain(name_of_current_user):
    for char in name_of_current_user:
        if not (char.isdigit() or char.isalpha() or char == "_" or char == "-"):
            return False
    return True


def no_redundant_symbols(name_of_current_user):
    if " " in name_of_current_user:
        return False
    return True


usernames = input().split(", ")

for current_username in usernames:
    if valid_username(current_username):
        print(current_username)
