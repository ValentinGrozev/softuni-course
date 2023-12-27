number_of_names = int(input())

record_with_names = set()

for name in range(number_of_names):
    current_name = input()
    if current_name not in record_with_names:
        record_with_names.add(current_name)
        print(current_name)
