cards_deck = input().split()
shuffles = int(input())

for shuffle in range(shuffles):
    middle_part = len(cards_deck) // 2
    left_part = cards_deck[:middle_part]
    right_part = cards_deck[middle_part:]
    shuffled_deck = []

    for card_index in range(len(left_part)):
        shuffled_deck.append(left_part[card_index])
        shuffled_deck.append(right_part[card_index])
    cards_deck = shuffled_deck

print(cards_deck)
