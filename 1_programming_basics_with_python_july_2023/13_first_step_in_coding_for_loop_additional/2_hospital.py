duration = int(input())

treated_patiens = 0
untreated_patiens = 0
doctors = 7

for days in range(1, duration + 1):
    number_of_patients = int(input())
    if days % 3 != 0:
        if number_of_patients < doctors:
            treated_patiens += number_of_patients
        else:
            treated_patiens += doctors
            untreated_patiens += number_of_patients - doctors
    if days % 3 == 0:
        if treated_patiens < untreated_patiens:
            doctors = doctors + 1
        if number_of_patients < doctors:
            treated_patiens += number_of_patients
        else:
            treated_patiens += doctors
            untreated_patiens += number_of_patients - doctors
print(f"Treated patients: {treated_patiens}.")
print(f"Untreated patients: {untreated_patiens}.")
