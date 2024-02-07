symbols_to_replace = ["-", ",", ".", "!", "?"]

with open("../12_1_files/file_1.txt", "r") as even_lines_file:
    text = even_lines_file.readlines()

for row in range(0, len(text), 2):
    for symbol in symbols_to_replace:
        text[row] = text[row].replace(symbol, "@")

    print(*text[row].split()[::-1])
