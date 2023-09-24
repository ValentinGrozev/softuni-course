number_of_open_tabs = int(input())
salary = int(input())

for _ in range(number_of_open_tabs):
    open_tabs_name = input()
    if open_tabs_name == "Facebook":
        salary -= 150
    elif open_tabs_name == "Instagram":
        salary -= 100
    elif open_tabs_name == "Reddit":
        salary -= 50
    if salary <= 0:
        print(f"You have lost your salary.")
        break
else:
    print(salary)


