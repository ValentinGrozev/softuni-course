concealed_message = input()
command = input().split(":|:")

while command[0] != "Reveal":
    action = command[0]
    if action == "InsertSpace":
        index = int(command[1])
        concealed_message = concealed_message[:index] + " " + concealed_message[index:]
        print(concealed_message)
    elif action == "Reverse":
        substring = command[1]
        if substring in concealed_message:
            reversed_substring = substring[::-1]
            concealed_message = concealed_message.replace(substring, "", 1)
            concealed_message = concealed_message + reversed_substring
            print(concealed_message)
        else:
            print("error")
    elif action == "ChangeAll":
        substring = command[1]
        new_substring = command[2]
        concealed_message = concealed_message.replace(substring, new_substring)
        print(concealed_message)
    command = input().split(":|:")

print(f"You have a new text message: {concealed_message}")
