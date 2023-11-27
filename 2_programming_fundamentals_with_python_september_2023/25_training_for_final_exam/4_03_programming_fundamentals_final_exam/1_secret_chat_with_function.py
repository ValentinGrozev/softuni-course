def insert_space_in_message(concealed_message, index):
    concealed_message = concealed_message[:index] + " " + concealed_message[index:]
    print(concealed_message)
    return concealed_message


def reverse_substring_in_message(concealed_message, substring):
    if substring in concealed_message:
        reversed_substring = substring[::-1]
        concealed_message = concealed_message.replace(substring, "", 1)
        concealed_message = concealed_message + reversed_substring
        print(concealed_message)
        return concealed_message
    else:
        print("error")
        return concealed_message


def change_all_occurrences(concealed_message, substring, new_substring):
    concealed_message = concealed_message.replace(substring, new_substring)
    print(concealed_message)
    return concealed_message


def main():

    concealed_message = input()
    command = input().split(":|:")

    while command[0] != "Reveal":
        action = command[0]
        if action == "InsertSpace":
            index = int(command[1])
            concealed_message = insert_space_in_message(concealed_message, index)
        elif action == "Reverse":
            substring = command[1]
            concealed_message = reverse_substring_in_message(concealed_message, substring)
        elif action == "ChangeAll":
            substring = command[1]
            new_substring = command[2]
            concealed_message = change_all_occurrences(concealed_message, substring, new_substring)
        command = input().split(":|:")

    print(f"You have a new text message: {concealed_message}")


main()
