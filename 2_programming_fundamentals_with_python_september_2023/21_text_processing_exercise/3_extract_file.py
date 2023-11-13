filepath = input().split("\\")

file_name_and_extension = ''

for path in filepath:
    if "." in path:
        file_name_and_extension += path

only_name_and_extension = file_name_and_extension.split(".")

print(f"File name: {only_name_and_extension[0]}")
print(f"File extension: {only_name_and_extension[1]}")
