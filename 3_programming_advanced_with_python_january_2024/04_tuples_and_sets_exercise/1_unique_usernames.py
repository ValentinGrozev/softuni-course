number_of_usernames = int(input())
unique_usernames = set()

for username in range(number_of_usernames):
    unique_usernames.add(input())

for current_username in unique_usernames:
    print(current_username)
