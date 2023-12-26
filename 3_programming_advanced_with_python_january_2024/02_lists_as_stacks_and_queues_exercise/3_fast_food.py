# First solution:
from collections import deque


def biggest_order(sequence_of_orders):
    print(max(sequence_of_orders))


def main():
    quantity_of_food = int(input())
    sequence_of_orders = [int(x) for x in input().split()]
    queue_of_orders = deque(sequence_of_orders)

    biggest_order(sequence_of_orders)
    while len(queue_of_orders) and quantity_of_food >= queue_of_orders[0]:
        quantity_of_food -= queue_of_orders.popleft()

    if len(queue_of_orders) != 0:
        print("Orders left:", end="")
        while queue_of_orders:
            print(f' {queue_of_orders.popleft()}', end="")
    else:
        print("Orders complete")


main()


# Second solution:
#
# from collections import deque
#
#
# def biggest_order(sequence_of_orders):
#     print(max(sequence_of_orders))
#
#
# def main():
#     quantity_of_food = int(input())
#     sequence_of_orders = [int(x) for x in input().split()]
#     queue_of_orders = deque(sequence_of_orders)
#
#     biggest_order(sequence_of_orders)
#     while len(queue_of_orders) and quantity_of_food >= queue_of_orders[0]:
#         quantity_of_food -= queue_of_orders.popleft()
#
#     if len(queue_of_orders) != 0:
#         queue_of_orders = [str(x) for x in queue_of_orders]
#         print(f"Orders left:", " ".join(queue_of_orders))
#     else:
#         print("Orders complete")
#
#
# main()
