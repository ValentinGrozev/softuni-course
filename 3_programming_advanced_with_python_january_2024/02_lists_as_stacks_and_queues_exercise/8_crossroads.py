from collections import deque

duration_of_green_lights = int(input())
green_light = duration_of_green_lights
free_window = int(input())
free_window_reset = free_window
command = input()

car_passed = 0
car_list = deque()

while command != "END":
    if command != "green":
        car_list.append(command)
    else:
        if car_list:
            duration_of_green_lights = green_light
            free_window = free_window_reset
            for _ in range(len(car_list)):
                current_car = car_list.popleft()
                duration_of_green_lights -= len(current_car)
                if duration_of_green_lights > 0:
                    car_passed += 1
                else:
                    if free_window >= abs(duration_of_green_lights):
                        car_passed += 1
                        break
                    else:
                        left_letter = abs(duration_of_green_lights) - free_window
                        crash_letter = len(current_car) - left_letter
                        print("A crash happened!")
                        print(f"{current_car} was hit at {list(current_car)[crash_letter]}.")
                        exit()

    command = input()

print("Everyone is safe.")
print(f"{car_passed} total cars passed the crossroads.")
