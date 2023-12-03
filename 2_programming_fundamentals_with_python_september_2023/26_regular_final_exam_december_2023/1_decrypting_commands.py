message_to_decrypt = input()
decrypting_commands = input().split(" ")

while decrypting_commands[0] != "Finish":
    action = decrypting_commands[0]
    if action == "Replace":
        current_char = decrypting_commands[1]
        new_char = decrypting_commands[2]
        if current_char in message_to_decrypt:
            message_to_decrypt = message_to_decrypt.replace(current_char, new_char)
            print(message_to_decrypt)
    elif action == "Cut":
        start_index = int(decrypting_commands[1])
        end_index = int(decrypting_commands[2])
        if start_index in range(len(message_to_decrypt)) and end_index in range(len(message_to_decrypt)):
            message_to_decrypt = message_to_decrypt[:start_index] + message_to_decrypt[end_index + 1:]
            print(message_to_decrypt)
        else:
            print("Invalid indices!")
    elif action == "Make":
        command = decrypting_commands[1]
        if command == "Upper":
            message_to_decrypt = message_to_decrypt.upper()
            print(message_to_decrypt)
        elif command == "Lower":
            message_to_decrypt = message_to_decrypt.lower()
            print(message_to_decrypt)
    elif action == "Check":
        string = decrypting_commands[1]
        if string in message_to_decrypt:
            print(f"Message contains {string}")
        else:
            print(f"Message doesn't contain {string}")
    elif action == "Sum":
        start_index = int(decrypting_commands[1])
        end_index = int(decrypting_commands[2])
        if 0 < start_index < len(message_to_decrypt) and 0 < end_index < len(message_to_decrypt):
            substring = message_to_decrypt[start_index: end_index + 1]
            ascII_sum = 0
            for char in substring:
                ascII_sum += ord(char)
            print(ascII_sum)
        else:
            print("Invalid indices!")

    decrypting_commands = input().split(" ")
