# first solution:

number_of_inputs = int(input())
unique_chemical_elements = set()

for _ in range(number_of_inputs):
    chemical_elements = input().split()
    for element in chemical_elements:
        unique_chemical_elements.add(element)

print("\n".join(unique_chemical_elements))
# print(*unique_chemical_elements, sep="\n")  --> Alternative way for print


# second solution:

# number_of_inputs = int(input())
# unique_chemical_elements = set()
#
# for _ in range(number_of_inputs):
#     unique_chemical_elements.update(input().split())
#
# print("\n".join(unique_chemical_elements))
