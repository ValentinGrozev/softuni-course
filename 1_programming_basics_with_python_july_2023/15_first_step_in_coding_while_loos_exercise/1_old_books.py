search_book = input()

counter = 0

while True:
    name_of_book = input()
    if name_of_book == search_book:
        break
    if name_of_book != search_book and name_of_book != "No More Books":
        counter += 1
    if name_of_book == "No More Books":
        break

if name_of_book == search_book:
    print(f"You checked {counter} books and found it.")
else:
    print(f"The book you search is not here!")
    print(f"You checked {counter} books.")



