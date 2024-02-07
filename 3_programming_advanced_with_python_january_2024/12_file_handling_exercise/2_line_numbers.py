from string import punctuation

with open("../12_1_files/file_2_input.txt", "r") as text_info:
    text = text_info.readlines()

output_file = open("../12_1_files/file_2_output.txt", "w")

for index, current_text in enumerate(text):
    letters = 0
    punctuation_marks = 0

    for current_symbol in current_text:
        if current_symbol.isalpha():
            letters += 1
        elif current_symbol in punctuation:
            punctuation_marks += 1

    output_file.write(f"Line {index + 1}: {current_text[:-1]} ({letters})({punctuation_marks})\n")


output_file.close()
