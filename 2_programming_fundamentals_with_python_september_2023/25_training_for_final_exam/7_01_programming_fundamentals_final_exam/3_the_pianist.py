def add_piece(pieces_details, piece, composer, key):
    if piece not in pieces_details:
        pieces_details[piece] = {"composer": "", "key": ""}
        pieces_details[piece]["composer"] = composer
        pieces_details[piece]["key"] = key
        print(f"{piece} by {composer} in {key} added to the collection!")
    else:
        print(f"{piece} is already in the collection!")


def remove_piece(pieces_details, piece):
    if piece in pieces_details:
        pieces_details.pop(piece)
        print(f"Successfully removed {piece}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")


def change_key(pieces_details, piece, new_key):
    if piece in pieces_details:
        pieces_details[piece]["key"] = new_key
        print(f"Changed the key of {piece} to {new_key}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")


def main():

    number_of_pieces = int(input())
    pieces_details = {}

    for current_piece in range(number_of_pieces):
        pieces_info = input().split("|")
        piece = pieces_info[0]
        composer = pieces_info[1]
        key = pieces_info[2]
        if piece not in pieces_details:
            pieces_details[piece] = {"composer": "", "key": ""}
        pieces_details[piece]["composer"] = composer
        pieces_details[piece]["key"] = key

    command = input().split("|")

    while command[0] != "Stop":
        action = command[0]
        if action == "Add":
            piece = command[1]
            composer = command[2]
            key = command[3]
            add_piece(pieces_details, piece, composer, key)
        elif action == "Remove":
            piece = command[1]
            remove_piece(pieces_details, piece)
        elif action == "ChangeKey":
            piece = command[1]
            new_key = command[2]
            change_key(pieces_details, piece, new_key)

        command = input().split("|")

    for current_piece, current_piece_info in pieces_details.items():
        print(f"{current_piece} -> Composer: {current_piece_info['composer']}, Key: {current_piece_info['key']}")


main()
