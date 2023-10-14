def are_employees_happy(happiness, multipy_happiness):
    upgraded_happiness = []
    for initially_happiness in happiness:
        improved_happiness = int(initially_happiness) * multipy_happiness
        upgraded_happiness.append(improved_happiness)
    sum_of_all_happiness = sum(upgraded_happiness)
    average_happiness = sum_of_all_happiness / len(happiness)
    happy_counter = 0
    for current_happiness in upgraded_happiness:
        if current_happiness >= average_happiness:
            happy_counter += 1
    if happy_counter >= int(len(happiness) / 2):
        return f"Score: {happy_counter}/{len(happiness)}. Employees are happy!"
    else:
        return f"Score: {happy_counter}/{len(happiness)}. Employees are not happy!"


employees_happiness = input().split()
improvement_factor = int(input())

print(are_employees_happy(employees_happiness, improvement_factor))
