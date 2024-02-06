from collections import deque

food_portions = [int(food) for food in input().split(", ")]
stamina = deque([int(stamina) for stamina in input().split(", ")])

mountain_peaks = deque([[80, "Vihren"], [90, "Kutelo"], [100, "Banski Suhodol"], [60, "Polezhan"], [70, "Kamenitza"]])


climbed_mountain_peaks = []

while food_portions and stamina and mountain_peaks:
    current_food = food_portions.pop()
    current_stamina = stamina.popleft()
    current_peak_info = mountain_peaks.popleft()
    current_peak_high = current_peak_info[0]
    current_peak_name = current_peak_info[1]

    result = current_food + current_stamina

    if result >= current_peak_high:
        climbed_mountain_peaks.append(current_peak_name)
    else:
        mountain_peaks.appendleft(current_peak_info)

if len(mountain_peaks) == 0:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if len(climbed_mountain_peaks) > 0:
    print("Conquered peaks:")
    print("\n".join(peak for peak in climbed_mountain_peaks))
