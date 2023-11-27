password = input()
command = input().split(" ")

while command[0] != "Done":
    action = command[0]
    if action == "TakeOdd":
        new_word = ""
        for letter_index, letter in enumerate(password):
            if letter_index % 2 != 0:
                new_word += letter
        password = new_word
        print(password)
    elif action == "Cut":
        index = int(command[1])
        length = int(command[2])
        text_to_cut = password[index:index + length]
        if text_to_cut in password:
            password = password.replace(text_to_cut, '', 1)
            print(password)
    elif action == "Substitute":
        substring = command[1]
        substitute = command[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")

    command = input().split(" ")

print(f"Your password is: {password}")
