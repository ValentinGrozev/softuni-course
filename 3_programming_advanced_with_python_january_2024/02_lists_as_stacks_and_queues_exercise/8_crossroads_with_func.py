from collections import deque

duration_of_green_lights = int(input())

free_window = int(input())
free_window_reset = free_window
command = input()

car_list = deque()
all_cars_passed = 0
green_light = duration_of_green_lights


# Returns number of passed cars for a single light switch
def start_window(car_queue, green_light_secs, yellow_light_secs):
    cars_passed = 0
    while len(car_queue) > 0:
        curr_car = car_queue.popleft()
        left_secs = green_light_secs - len(curr_car)
        if left_secs > 0:
            green_light_secs -= len(curr_car)
            cars_passed += 1
        else:
            # car can move from crossroads before red signal
            if yellow_light_secs >= abs(left_secs):
                cars_passed += 1
                break
            else:
                left_letters = abs(left_secs) - yellow_light_secs
                crash_letter = curr_car[len(curr_car) - left_letters]
                return False, (curr_car, crash_letter)

    return True, cars_passed


while command != "END":
    if command != "green":
        car_list.append(command)
    else:
        success, args = start_window(car_list, duration_of_green_lights, free_window)

        if success:
            curr_cars_passed = args
            all_cars_passed += curr_cars_passed
        else:
            crashed_car, crashed_letter = args
            print("A crash happened!")
            print(f"{crashed_car} was hit at {crashed_letter}.")
            exit()
    command = input()

print("Everyone is safe.")
print(f"{all_cars_passed} total cars passed the crossroads.")
