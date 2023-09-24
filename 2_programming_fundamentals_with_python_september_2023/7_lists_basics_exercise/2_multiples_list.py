factor = int(input())
count = int(input())

multiples_list = []
multiples_factor = 0

for numbers in range(count):
    multiples_factor += factor
    multiples_list.append(multiples_factor)

print(multiples_list)
