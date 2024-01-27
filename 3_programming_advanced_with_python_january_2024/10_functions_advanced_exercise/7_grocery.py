# first solution:
def grocery_store(**kwargs):
    sorted_elements = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    return "\n".join(f"{product}: {quantity}" for product, quantity in sorted_elements)


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))

# first solution without comprehension:

# def grocery_store(**kwargs):
#     sorted_elements = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
#     products = []
#     for product, quantity in sorted_elements:
#         products.append(f"{product}: {quantity}")
#     return "\n".join(products)
#
#
# print(grocery_store(
#     bread=5,
#     pasta=12,
#     eggs=12,
# ))
