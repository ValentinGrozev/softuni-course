length_sm = int(input())
width_sm = int(input())
height_sm = int(input())
percent_of_fill = float(input())

volume_sm = length_sm * width_sm * height_sm
volume_dm = volume_sm / 1000

final_volume = volume_dm - (volume_dm * percent_of_fill / 100)

print(final_volume)