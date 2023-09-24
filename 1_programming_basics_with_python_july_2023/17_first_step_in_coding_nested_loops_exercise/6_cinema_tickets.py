name_of_movie = input()

ticket_counter = 0
all_tickets = 0
student_ticket = 0
standard_ticket = 0
kids_ticket = 0

while name_of_movie != "Finish":
    movie = name_of_movie
    free_spaces = int(input())
    ticket_type = input()

    while ticket_type != "End":
        ticket_type = ticket_type
        ticket_counter += 1
        all_tickets += 1

        if ticket_type == "student":
            student_ticket += 1
        elif ticket_type == "standard":
            standard_ticket += 1
        elif ticket_type == "kid":
            kids_ticket += 1

        if ticket_counter == free_spaces:
            break
        ticket_type = input()

    percentage_tickets = ticket_counter / free_spaces * 100
    print(f"{name_of_movie} - {percentage_tickets:.2f}% full.")

    name_of_movie = input()
    ticket_counter = 0

percentage_student_ticket = student_ticket / all_tickets * 100
percentage_standard_ticket = standard_ticket / all_tickets * 100
percentage_kids_ticket = kids_ticket / all_tickets * 100

print(f"Total tickets: {all_tickets}")
print(f"{percentage_student_ticket:.2f}% student tickets.")
print(f"{percentage_standard_ticket:.2f}% standard tickets.")
print(f"{percentage_kids_ticket:.2f}% kids tickets.")
