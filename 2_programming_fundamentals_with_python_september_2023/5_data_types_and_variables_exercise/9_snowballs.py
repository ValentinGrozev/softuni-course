number_of_balls = int(input())

max_weight_of_snowball = 0
max_time_needed = 0
max_quality = 0
max_value = 0

for snowballs in range(number_of_balls):
    weight_of_snowball = int(input())
    time_needed_for_snowball = int(input())
    quality_of_snowball = int(input())
    value_of_snowball = (weight_of_snowball / time_needed_for_snowball) ** quality_of_snowball
    if value_of_snowball > max_value:
        max_value = value_of_snowball
        max_weight_of_snowball = weight_of_snowball
        max_time_needed = time_needed_for_snowball
        max_quality = quality_of_snowball

print(f"{max_weight_of_snowball} : {max_time_needed} = {max_value:.0f} ({max_quality})")
