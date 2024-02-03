from collections import deque

tools = deque([int(tool) for tool in input().split()])
substances = [int(substance) for substance in input().split()]
challenges = [int(challenge) for challenge in input().split()]
artifact_found = False

while tools and substances:
    current_tool = tools.popleft()
    current_substance = substances.pop()

    result = current_tool * current_substance

    if result in challenges:
        challenges.remove(result)
    else:
        current_tool += 1
        current_substance -= 1

        tools.append(current_tool)

        if current_substance > 0:
            substances.append(current_substance)

    if not challenges:
        artifact_found = True
        break

if artifact_found:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")
else:
    print("Harry is lost in the temple. Oblivion awaits him.")

if tools:
    print(f"Tools: {', '.join([str(tool) for tool in tools])}")

if substances:
    print(f"Substances: {', '.join([str(substance) for substance in substances])}")

if challenges:
    print(f"Challenges: {', '.join([str(challenge) for challenge in challenges])}")
