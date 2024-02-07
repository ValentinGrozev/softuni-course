import os


def create_file(name):
    with open(f"../12_1_files/{name}", "w"):
        pass


def add_text_in_file(name, text):
    with open(f"../12_1_files/{name}", "a") as current_file:
        current_file.write(f"{text}\n")


def replace_olf_with_new_content(name, old_text, new_text):
    try:
        with open(f"../12_1_files/{name}", "r+") as current_file:
            text = current_file.read()
            text = text.replace(old_text, new_text)

            current_file.seek(0)
            current_file.write(text)
            current_file.truncate()

    except FileNotFoundError:
        print("An error occurred")


def delete_file(name):
    try:
        os.remove(f"../12_1_files/{name}")
    except FileNotFoundError:
        print("An error occurred")


def main():
    command = input()

    while command != "End":
        command_information = command.split("-")
        command_title = command_information[0]

        if command_title == "Create":
            file_name = command_information[1]
            create_file(file_name)

        elif command_title == "Add":
            file_name = command_information[1]
            content = command_information[2]
            add_text_in_file(file_name, content)

        elif command_title == "Replace":
            file_name = command_information[1]
            old_file_to_replace = command_information[2]
            new_file = command_information[3]
            replace_olf_with_new_content(file_name, old_file_to_replace, new_file)

        elif command_title == "Delete":
            file_name = command_information[1]
            delete_file(file_name)

        command = input()


main()
