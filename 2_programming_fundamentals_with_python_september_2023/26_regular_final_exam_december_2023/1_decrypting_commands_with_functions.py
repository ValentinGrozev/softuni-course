def replace(message_to_decrypt, current_char, new_char):
    if current_char in message_to_decrypt:
        message_to_decrypt = message_to_decrypt.replace(current_char, new_char)
        print(message_to_decrypt)
    return message_to_decrypt


def cut(message_to_decrypt, start_index, end_index):
    if start_index in range(len(message_to_decrypt)) and end_index in range(len(message_to_decrypt)):
        message_to_decrypt = message_to_decrypt[:start_index] + message_to_decrypt[end_index + 1:]
        print(message_to_decrypt)
    else:
        print("Invalid indices!")
    return message_to_decrypt


def make(message_to_decrypt, command):
    if command == "Upper":
        message_to_decrypt = message_to_decrypt.upper()
        print(message_to_decrypt)
    elif command == "Lower":
        message_to_decrypt = message_to_decrypt.lower()
        print(message_to_decrypt)
    return message_to_decrypt


def check(message_to_decrypt, string):
    if string in message_to_decrypt:
        print(f"Message contains {string}")
    else:
        print(f"Message doesn't contain {string}")
    return message_to_decrypt


def summing(message_to_decrypt, start_index, end_index):
    if 0 < start_index < len(message_to_decrypt) and 0 < end_index < len(message_to_decrypt):
        substring = message_to_decrypt[start_index: end_index + 1]
        ascii_table_sum = 0
        for char in substring:
            ascii_table_sum += ord(char)
        print(ascii_table_sum)
    else:
        print("Invalid indices!")


def main():
    message_to_decrypt = input()
    decrypting_commands = input().split(" ")

    while decrypting_commands[0] != "Finish":
        action = decrypting_commands[0]
        if action == "Replace":
            current_char = decrypting_commands[1]
            new_char = decrypting_commands[2]
            message_to_decrypt = replace(message_to_decrypt, current_char, new_char)
        elif action == "Cut":
            start_index = int(decrypting_commands[1])
            end_index = int(decrypting_commands[2])
            message_to_decrypt = cut(message_to_decrypt, start_index, end_index)
        elif action == "Make":
            command = decrypting_commands[1]
            message_to_decrypt = make(message_to_decrypt, command)
        elif action == "Check":
            string = decrypting_commands[1]
            message_to_decrypt = check(message_to_decrypt, string)
        elif action == "Sum":
            start_index = int(decrypting_commands[1])
            end_index = int(decrypting_commands[2])
            summing(message_to_decrypt, start_index, end_index)

        decrypting_commands = input().split(" ")


main()
