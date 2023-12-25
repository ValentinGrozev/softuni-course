from collections import deque

customer_name = input()
customers_names_list = deque()

while customer_name != "End":
    if customer_name == "Paid":
        while len(customers_names_list) != 0:
            print(customers_names_list.popleft())
    else:
        customers_names_list.append(customer_name)
    customer_name = input()

print(f"{len(customers_names_list)} people remaining.")
