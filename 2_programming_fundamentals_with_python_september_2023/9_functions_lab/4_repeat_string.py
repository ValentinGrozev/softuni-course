def multiply_string(current_string: str, multiply: int) -> str:
    return current_string * multiply


string = input()
counter = int(input())
print(multiply_string(string, counter))