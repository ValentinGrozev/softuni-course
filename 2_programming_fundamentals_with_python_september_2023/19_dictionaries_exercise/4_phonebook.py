contact_information = input()

phone_book = {}

while "-" in contact_information:
    contact_details = contact_information.split("-")
    contact_name = contact_details[0]
    phone_number = contact_details[1]
    if contact_name not in phone_book:
        phone_book[contact_name] = phone_number
    else:
        phone_book[contact_name] = phone_number

    contact_information = input()

number_of_searched_contacts = int(contact_information)

for number_of_searched_contacts in range(number_of_searched_contacts):
    searched_contact_name = input()
    if searched_contact_name in phone_book.keys():
        print(f"{searched_contact_name} -> {phone_book[searched_contact_name]}")
    else:
        print(f"Contact {searched_contact_name} does not exist.")
