budget = float(input())
video_count = int(input())
processor_count = int(input())
ram_count = int(input())

price_for_video = 250
price_for_processor = 0.35 * (price_for_video * video_count)
price_for_ram = 0.1 * (price_for_video * video_count)

total_cost = video_count * price_for_video + processor_count * price_for_processor + ram_count * price_for_ram

if video_count > processor_count:
    total_cost = 0.85 * total_cost

diff = abs(budget - total_cost)

if budget >= total_cost:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")