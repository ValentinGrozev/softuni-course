from math import floor

first_player_time = int(input())
second_player_time = int(input())
third_player_time = int(input())

total_time = first_player_time + second_player_time + third_player_time

minutes = total_time // 60
seconds = total_time % 60

minutes = floor(minutes)

if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")


