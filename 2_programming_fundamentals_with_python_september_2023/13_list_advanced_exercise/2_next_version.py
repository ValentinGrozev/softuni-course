current_version = input().split(".")

number = "".join(current_version)
next_version = int(number) + 1
print(".".join(str(next_version)))
