first_employee_efficiency = int(input())
second_employee_efficiency = int(input())
third_employee_efficiency = int(input())
students_count = int(input())

total_employee_efficiency = first_employee_efficiency + second_employee_efficiency + third_employee_efficiency
hours_needed_to_answer = 0

while students_count > 0:
    hours_needed_to_answer += 1
    if hours_needed_to_answer % 4 == 0:
        pass
    else:
        students_count -= total_employee_efficiency

print(f"Time needed: {hours_needed_to_answer}h.")
