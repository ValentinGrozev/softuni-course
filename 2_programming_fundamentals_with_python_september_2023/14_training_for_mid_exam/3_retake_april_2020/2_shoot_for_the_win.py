value_of_targets = input().split()
index_of_target = input()

value_of_integer_targets = [int(number) for number in value_of_targets]
count_ot_shot_targets = 0

while index_of_target != "End":
    index_of_target = int(index_of_target)
    if index_of_target <= len(value_of_integer_targets) - 1:
        for index in range(len(value_of_integer_targets)):
            number = value_of_integer_targets[index_of_target]
            value_of_integer_targets[index_of_target] = -1
            count_ot_shot_targets += 1
            for number_index, current_number in enumerate(value_of_integer_targets):
                if current_number == -1:
                    continue
                if current_number > number:
                    current_number = current_number - number
                    value_of_integer_targets[number_index] = current_number
                else:
                    current_number = current_number + number
                    value_of_integer_targets[number_index] = current_number
            break
    index_of_target = input()

print(f"Shot targets: {count_ot_shot_targets} -> {' '.join(str(number) for number in value_of_integer_targets)}")
