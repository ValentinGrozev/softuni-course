number_of_guests = int(input())

reservations = set()

for current_reservation in range(number_of_guests):
    reservation_code = input()
    reservations.add(reservation_code)

guests_came_to_the_party = input()

while guests_came_to_the_party != "END":
    reservations.remove(guests_came_to_the_party)
    guests_came_to_the_party = input()

print(len(reservations))
reservations = sorted(reservations)
for reservation_code in reservations:
    print(reservation_code)
