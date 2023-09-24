last_sector = input()
number_of_rows_in_first_sector = int(input())
number_of_seats_in_odd_sector = int(input())

first_sector = "A"
first_sector_in_ASCII = ord(first_sector)
last_sector_in_ASCII = ord(last_sector)
counter = 0
rows = 1
additional_row = 1

for sectors in range(first_sector_in_ASCII, last_sector_in_ASCII + 1):
    while rows <= number_of_rows_in_first_sector:
        if rows % 2 == 0:
            for seats in range(1, number_of_seats_in_odd_sector + 3):
                counter += 1
                print(f"{chr(sectors)}{rows}{chr(seats + 96)}")
        else:
            for seats in range(1, number_of_seats_in_odd_sector + 1):
                counter += 1
                print(f"{chr(sectors)}{rows}{chr(seats + 96)}")
        rows += 1
    rows = 1
    number_of_rows_in_first_sector += 1
print(counter)
