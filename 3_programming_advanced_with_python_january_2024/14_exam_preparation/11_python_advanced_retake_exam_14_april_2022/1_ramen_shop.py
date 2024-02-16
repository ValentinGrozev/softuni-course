from collections import deque

bowls_of_ramen = [int(ramen) for ramen in input().split(", ")]
customers = deque([int(customer) for customer in input().split(", ")])

while bowls_of_ramen and customers:
    current_bowl_of_ramen = bowls_of_ramen.pop()
    current_customer = customers.popleft()

    if current_bowl_of_ramen > current_customer:
        current_bowl_of_ramen -= current_customer
        bowls_of_ramen.append(current_bowl_of_ramen)
    elif current_bowl_of_ramen < current_customer:
        current_customer -= current_bowl_of_ramen
        customers.appendleft(current_customer)

if not customers:
    print("Great job! You served all the customers.")

if bowls_of_ramen:
    print(f"Bowls of ramen left: {', '.join([str(ramen) for ramen in bowls_of_ramen])}")
if not bowls_of_ramen and customers:
    print(f"Out of ramen! You didn't manage to serve all customers.")

if customers:
    print(f"Customers left: {', '.join([str(customer) for customer in customers])}")
