import re


def find_name(text):
    pattern = r"[A-Za-z]+"
    matches = re.findall(pattern, text)
    return "".join(matches)


def find_score(text):
    pattern = r"[0-9]"
    matches = re.findall(pattern, text)
    final_score_list = [int(number) for number in matches]
    final_score = sum(final_score_list)
    return final_score


list_of_participants = input().split(", ")
random_text = input()

distances = {participant: 0 for participant in list_of_participants}

while random_text != "end of race":
    name_of_current_participant = find_name(random_text)
    score_of_current_participant = find_score(random_text)
    if name_of_current_participant in distances:
        distances[name_of_current_participant] += score_of_current_participant

    random_text = input()

sorted_distance = sorted(distances.items(), key=lambda x: x[1], reverse=True)
print(f"1st place: {sorted_distance[0][0]}")
print(f"2nd place: {sorted_distance[1][0]}")
print(f"3rd place: {sorted_distance[2][0]}")
