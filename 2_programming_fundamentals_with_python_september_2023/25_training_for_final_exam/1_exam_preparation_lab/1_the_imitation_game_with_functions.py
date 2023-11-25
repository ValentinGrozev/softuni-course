def move_letters(message, letters):
    message = message[letters:] + message[:letters]
    return message


def insert_letter(message, current_index, letter):
    message = message[:current_index] + letter + message[current_index:]
    return message


def change_all(message, old_string, new_string):
    message = message.replace(old_string, new_string)
    return message


def main():

    encrypted_message = input()
    command = input().split("|")

    while command[0] != "Decode":
        action = command[0]
        if action == "Move":
            letters_to_move = int(command[1])
            encrypted_message = move_letters(encrypted_message, letters_to_move)
        elif action == "Insert":
            index = int(command[1])
            value = command[2]
            encrypted_message = insert_letter(encrypted_message, index, value)
        elif action == "ChangeAll":
            current_string = command[1]
            new_string = command[2]
            encrypted_message = change_all(encrypted_message, current_string, new_string)

        command = input().split("|")

    print(f"The decrypted message is: {encrypted_message}")


main()
