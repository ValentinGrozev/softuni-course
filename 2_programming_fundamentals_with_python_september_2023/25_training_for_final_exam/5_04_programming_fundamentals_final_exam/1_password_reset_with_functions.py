def take_odd_characters(password):
    new_word = ""
    for letter_index, letter in enumerate(password):
        if letter_index % 2 != 0:
            new_word += letter
    password = new_word
    print(password)
    return password


def cut_string(password, index, length):
    text_to_cut = password[index:index + length]
    if text_to_cut in password:
        password = password.replace(text_to_cut, '', 1)
        print(password)
        return password


def substitute_string(password, substring, substitute):
    if substring in password:
        password = password.replace(substring, substitute)
        print(password)
        return password
    else:
        print("Nothing to replace!")
        return password


def main():
    password = input()
    command = input().split(" ")

    while command[0] != "Done":
        action = command[0]
        if action == "TakeOdd":
            password = take_odd_characters(password)
        elif action == "Cut":
            index = int(command[1])
            length = int(command[2])
            password = cut_string(password, index, length)
        elif action == "Substitute":
            substring = command[1]
            substitute = command[2]
            password = substitute_string(password, substring, substitute)

        command = input().split(" ")

    print(f"Your password is: {password}")


main()
