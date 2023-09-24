pieces_left = int(input()) * int(input())

cmd = input()
while cmd != "STOP":
    pieces_left -= int(cmd)

    if 0 > pieces_left:
        print(f"No more cake left! You need {pieces_left * -1} pieces more.")
        break

    cmd = input()

if pieces_left > 0:
    print(f"{pieces_left} pieces are left.")