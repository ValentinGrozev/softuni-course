def forecast(*towns_and_weather):
    weather_information = {}

    for town, weather in towns_and_weather:
        if weather not in weather_information:
            weather_information[weather] = []
        weather_information[weather].append(town)

    weathers = {
        "Sunny": 1,
        "Cloudy": 2,
        "Rainy": 3}

    sorted_weather_information = sorted(weather_information.items(), key=lambda x: weathers[x[0]])

    result = ''

    for town, weather in sorted_weather_information:
        for current_weather in sorted(weather):
            result += f"{current_weather} - {town}\n"

    return result


print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))
