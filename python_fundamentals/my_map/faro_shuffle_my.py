deck_of_cards = input().split()
shuffles_count = int(input())

for shuffles in range(shuffles_count):
    first_deck = deck_of_cards[0:len(deck_of_cards) // 2]
    second_deck = deck_of_cards[len(deck_of_cards) // 2:]
    deck_after_shuffle = []
    for index in range(len(first_deck)):
        deck_after_shuffle.append(first_deck[index])
        deck_after_shuffle.append(second_deck[index])
    deck_of_cards = deck_after_shuffle
print(deck_of_cards)