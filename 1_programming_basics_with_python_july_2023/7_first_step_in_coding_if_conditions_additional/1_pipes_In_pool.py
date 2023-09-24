pool_volume = int(input())
flow_rate_of_the_first_pipe_per_hour = int(input())
flow_rate_of_the_second_pipe_per_hour = int(input())
hours_away = float(input())

first_pipe_liters_for_hours_away = flow_rate_of_the_first_pipe_per_hour * hours_away
second_pipe_liters_for_hours_away = flow_rate_of_the_second_pipe_per_hour * hours_away

volume_fill = first_pipe_liters_for_hours_away + second_pipe_liters_for_hours_away
percentage = (volume_fill / pool_volume) * 100

first_pipe_fill_percentage = (first_pipe_liters_for_hours_away / volume_fill) * 100
second_pipe_fill_percentage = (second_pipe_liters_for_hours_away / volume_fill) * 100

diff = abs(pool_volume - volume_fill)

if pool_volume < volume_fill:
    print(f"For {hours_away} hours the pool overflows with {diff:.2f} liters.")
else:
    print(f"The pool is {percentage:.2f}% full. Pipe 1: {first_pipe_fill_percentage:.2f}%. Pipe 2: {second_pipe_fill_percentage:.2f}%.")
