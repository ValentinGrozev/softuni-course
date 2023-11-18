import re

dates_to_check = input()
pattern = r"\d{2}\.[A-Z]{1}[a-z]{2}\.\d{4}|\d{2}\-[A-Z]{1}[a-z]{2}\-\d{4}|\d{2}\/[A-Z]{1}[a-z]{2}\/\d{4}"

matches = re.findall(pattern, dates_to_check)

for element in range(len(matches)):
    match_date = (matches[element])
    if "/" in match_date:
        final_match_date = match_date.split("/")
        day = final_match_date[0]
        month = final_match_date[1]
        year = final_match_date[2]
        print(f"Day: {day}, Month: {month}, Year: {year}")
    elif "." in match_date:
        final_match_date = match_date.split(".")
        day = final_match_date[0]
        month = final_match_date[1]
        year = final_match_date[2]
        print(f"Day: {day}, Month: {month}, Year: {year}")
    elif "-" in match_date:
        final_match_date = match_date.split("-")
        day = final_match_date[0]
        month = final_match_date[1]
        year = final_match_date[2]
        print(f"Day: {day}, Month: {month}, Year: {year}")
