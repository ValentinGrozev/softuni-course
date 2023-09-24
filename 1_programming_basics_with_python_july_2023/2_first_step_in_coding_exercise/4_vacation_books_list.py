number_of_pages = int(input())
pages_per_hour = int(input())
days = int(input())

total_hours_per_book = number_of_pages // pages_per_hour
total_hours_per_day = total_hours_per_book / days

print(total_hours_per_day)
