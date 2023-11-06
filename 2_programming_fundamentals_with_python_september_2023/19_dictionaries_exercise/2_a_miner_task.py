resource = input()

resource_collection = {}

while resource != "stop":
    resource_name = resource
    resource_quantity = int(input())
    if resource_name not in resource_collection:
        resource_collection[resource_name] = 0
    resource_collection[resource_name] += resource_quantity

    resource = input()

for resource, quantity in resource_collection.items():
    print(f"{resource} -> {quantity}")
