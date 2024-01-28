# first solution:
def math_operations(*numbers, **result):
    for index in (range(len(numbers))):
        if index % len(result) == 0:
            result["a"] += numbers[index]
        elif index % len(result) == 1:
            result["s"] -= numbers[index]
        elif index % len(result) == 2:
            try:
                result["d"] /= numbers[index]
            except ZeroDivisionError:
                continue
        elif index % len(result) == 3:
            result["m"] *= numbers[index]

    return "\n".join(f"{key}: {value:.1f}" for key, value in sorted(result.items(), key=lambda x: (-x[1], x[0])))


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))


# second solution:
# def math_operations(*numbers, **result):
#     keys = list(result.keys())
#
#     for index in range(len(numbers)):
#         key = keys[index % 4]
#
#         if key == "a":
#             result[key] += numbers[index]
#         elif key == "s":
#             result[key] -= numbers[index]
#         elif key == "d":
#             if numbers[index] != 0:
#                 result[key] /= numbers[index]
#         elif key == "m":
#             result[key] *= numbers[index]
#
#     result = sorted(result.items(), key=lambda x: (-x[1], x[0]))
#
#     return "\n".join(f"{k}: {v:.1f}" for k, v in result)
