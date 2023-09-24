steps = input()
all_steps = 0
flag = False

while steps != "Going home":
    steps = int(steps)
    all_steps += steps
    if all_steps > 10000:
        diff = abs(all_steps - 10000)
        print("Goal reached! Good job!")
        print(f"{diff} steps over the goal!")
        break
    steps = input()

if steps == "Going home":
    steps = int(input())
    all_steps += steps
    if all_steps >= 10000:
        diff = all_steps - 10000
        print("Goal reached! Good job!")
        print(f"{diff} steps over the goal!")
    else:
        diff = abs(all_steps - 10000)
        print(f"{diff} more steps to reach goal.")




