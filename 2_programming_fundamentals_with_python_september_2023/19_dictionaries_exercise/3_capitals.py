country_names = input().split(", ")
country_capitals = input().split(", ")

final_dict = dict(zip(country_names, country_capitals))

for country, capital in final_dict.items():
    print(f"{country} -> {capital}")
