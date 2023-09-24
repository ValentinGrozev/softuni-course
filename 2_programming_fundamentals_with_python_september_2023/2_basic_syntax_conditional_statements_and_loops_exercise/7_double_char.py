input_text = input()

while input_text != "End":
    if input_text != "SoftUni":
        output_text = ""
        for i in input_text:
            output_text += i*2
        print(output_text)
    input_text = input()
