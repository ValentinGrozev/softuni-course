def data_types_and_values(data_type, some_value):
    if data_type == "int":
        some_value = int(some_value)
        result = some_value * 2
        return result
    elif data_type == "real":
        some_value = float(some_value)
        result = some_value * 1.50
        return f"{result:.2f}"
    elif data_type == "string":
        return f"${some_value}$"


type_of_data = input()
value = input()
print(data_types_and_values(type_of_data, value))
