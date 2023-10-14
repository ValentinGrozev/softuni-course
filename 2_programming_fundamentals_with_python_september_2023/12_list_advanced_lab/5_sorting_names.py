def sorted_names(list_with_names):
    list_with_names.sort()
    list_with_names.sort(key=len, reverse=True)
    return names


names = input().split(", ")

print(sorted_names(names))