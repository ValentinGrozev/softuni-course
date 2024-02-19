def set_cover(curr_universe, curr_sets):
    all_used_sets = []

    while curr_universe:
        best_set = max(curr_sets, key=lambda s: len(curr_universe.intersection(s)))
        all_used_sets.append(best_set)
        curr_universe -= best_set

    return all_used_sets


universe = {int(x) for x in input().split(", ")}
number_of_sets = int(input())
sets = [{int(current_set) for current_set in input().split(", ")}for _ in range(number_of_sets)]

used_sets = (set_cover(universe, sets))

if used_sets is None:
    print("No solution exist")
else:
    for index in range(len(used_sets)):
        used_sets[index] = sorted(used_sets[index])

    print(f"Sets to take ({len(used_sets)}):")

    for final_set in used_sets:
        print('{' + f" {', '.join(str(number) for number in final_set)} " + '}')
