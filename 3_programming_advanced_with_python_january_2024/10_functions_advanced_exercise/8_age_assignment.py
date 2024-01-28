# first solution - optimal:

def age_assignment(*names, **kwargs):
    names_list = {}
    for name in names:
        first_letter = name[0]
        if first_letter in kwargs:
            age = kwargs[first_letter]
            names_list[name] = age

    return '\n'.join(f"{name} is {age} years old." for name, age in sorted(names_list.items(), key=lambda x: x[0]))


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))


# second solution - time inefficient:
# def age_assignment(*names, **kwargs):
#     names_list = {}
#     for name in names:
#         if name not in names_list:
#             names_list[name] = 0
#
#     for letter, age in kwargs.items():
#         for name in names_list:
#             if name.startswith(letter):
#                 names_list[name] = age
#
#     return '\n'.join(f"{name} is {age} years old." for name, age in sorted(names_list.items(), key=lambda x: x[0]))
#
#
# print(age_assignment("Peter", "George", G=26, P=19))
# print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
