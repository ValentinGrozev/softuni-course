encrypted_message = input()
command = input().split("|")

while command[0] != "Decode":
    action = command[0]
    if action == "Move":
        letters_to_move = int(command[1])
        encrypted_message = encrypted_message[letters_to_move:] + encrypted_message[:letters_to_move]
    elif action == "Insert":
        index = int(command[1])
        value = command[2]
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]
    elif action == "ChangeAll":
        current_string = command[1]
        new_string = command[2]
        encrypted_message = encrypted_message.replace(current_string, new_string)

    command = input().split("|")

print(f"The decrypted message is: {encrypted_message}")
