guests_and_meals_response = input().split("-")
dinner_response = {}

dislike_meals = 0

while guests_and_meals_response[0] != "Stop":
    response = guests_and_meals_response[0]
    guest_name = guests_and_meals_response[1]
    meal = guests_and_meals_response[2].strip()
    if response == "Like":
        if guest_name not in dinner_response:
            dinner_response[guest_name] = []
        if meal not in dinner_response[guest_name]:
            dinner_response[guest_name].append(meal)
    elif response == "Dislike":
        if guest_name not in dinner_response:
            print(f"{guest_name} is not at the party.")
        elif meal not in dinner_response[guest_name]:
            print(f"{guest_name} doesn't have the {meal} in his/her collection.")
        elif meal in dinner_response[guest_name]:
            dinner_response[guest_name].remove(meal)
            dislike_meals += 1
            print(f"{guest_name} doesn't like the {meal}.")

    guests_and_meals_response = input().split("-")

for guest, meals in dinner_response.items():
    print(f"{guest}: {', '.join(meals)}")
print(f"Unliked meals: {dislike_meals}")
