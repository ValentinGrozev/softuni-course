width = int(input())
length = int(input())

number_of_pieces_cake = width * length

piece_of_cake = input()

count_pieces = 0

while piece_of_cake != "STOP":
    piece_of_cake = int(piece_of_cake)
    count_pieces += piece_of_cake
    if count_pieces >= number_of_pieces_cake:
        diff = abs(number_of_pieces_cake - count_pieces)
        print(f"No more cake left! You need {diff} pieces more.")
        break
    piece_of_cake = input()

if piece_of_cake == "STOP":
    diff = abs(number_of_pieces_cake - count_pieces)
    print(f"{diff} pieces are left.")