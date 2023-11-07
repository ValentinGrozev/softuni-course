information = input()

company_employee_register = {}

while "->" in information:
    company_name_and_employee_id = information.split(" -> ")
    company_name = company_name_and_employee_id[0]
    employee_id = company_name_and_employee_id[1]
    if company_name not in company_employee_register:
        company_employee_register[company_name] = []
    if employee_id in company_employee_register[company_name]:
        information = input()
        continue
    else:
        company_employee_register[company_name].append(employee_id)

    information = input()

for name_of_company, name_of_employees in company_employee_register.items():
    print(f"{name_of_company}")
    for name in name_of_employees:
        print(f"-- {name}")
