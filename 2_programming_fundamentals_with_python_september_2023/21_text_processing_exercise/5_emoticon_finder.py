text = input().split()

emojy_filter = ""

for element in range(len(text)):
    if ":" in text[element]:
        emojy_filter += text[element]

for char_index in range(len(emojy_filter)):
    if ":" in emojy_filter[char_index]:
        print(f":{emojy_filter[char_index + 1]}")


# text = input()
# for index in range(len(text)):
#     if text[index] == ":":
#         print(f":{text[index + 1]}")