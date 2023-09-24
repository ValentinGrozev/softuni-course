number_junior_velo = int(input())
number_senior_velo = int(input())
type_track = input()

cost_junior = 0
cost_senior = 0
expenses = 0

if type_track == "trail":
    cost_junior = number_junior_velo * 5.50
    cost_senior = number_senior_velo * 7
    total_cost = cost_junior + cost_senior
    expenses = 0.05 * total_cost
    final_sum = total_cost - expenses
    print(f"{final_sum:.2f}")
elif type_track == "cross-country":
    number_of_all_velo = number_junior_velo + number_senior_velo
    if number_of_all_velo >= 50:
        cost_junior = number_junior_velo * (8 * 0.75)
        cost_senior = number_senior_velo * (9.5 * 0.75)
        total_cost = cost_junior + cost_senior
        expenses = 0.05 * total_cost
        final_sum = total_cost - expenses
        print(f"{final_sum:.2f}")
    else:
        cost_junior = number_junior_velo * 8
        cost_senior = number_senior_velo * 9.5
        total_cost = cost_junior + cost_senior
        expenses = 0.05 * total_cost
        final_sum = total_cost - expenses
        print(f"{final_sum:.2f}")
elif type_track == "downhill":
    cost_junior = number_junior_velo * 12.25
    cost_senior = number_senior_velo * 13.75
    total_cost = cost_junior + cost_senior
    expenses = 0.05 * total_cost
    final_sum = total_cost - expenses
    print(f"{final_sum:.2f}")
elif type_track == "road":
    cost_junior = number_junior_velo * 20
    cost_senior = number_senior_velo * 21.50
    total_cost = cost_junior + cost_senior
    expenses = 0.05 * total_cost
    final_sum = total_cost - expenses
    print(f"{final_sum:.2f}")