animal_type = input()

list_1 = ["dog"]
list_2 = ["crocodile", "tortoise", "snake"]

if animal_type in list_1:
    print("mammal")
elif animal_type in list_2:
    print("reptile")
else:
    print("unknown")