from math import floor

world_record_sec = float(input())
distance_in_meter = float(input())
time_per_meter = float(input())

water_resist_per_15m = 12.5

total_time = distance_in_meter * time_per_meter
additional_time = floor(distance_in_meter // 15) * 12.5
final_time = total_time + additional_time

diff = abs(world_record_sec - final_time)

if final_time < world_record_sec:
    print(f" Yes, he succeeded! The new world record is {final_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {diff:.2f} seconds slower.")


