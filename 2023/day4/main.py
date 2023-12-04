from pathlib import Path

with open(Path(__file__).parent / "data") as file:
    cards = [[1, sum([1 if w in numbers else 0 for w in winners])] for winners,numbers in [[sorted(list(map(int, digits))) for digits in [card.strip().split() for card in line.rstrip('\n\r').split(':')[1].split('|')]] for line in file.readlines()]]
    
    number_of_cards = 0
    for current_card_number,card in enumerate(cards):
        number_of_cards += card[0]
        for copy in range(0, card[0]):
            for new_copy_id in range(current_card_number + 1, current_card_number + 1 + card[1]):
                cards[new_copy_id][0] += 1

    print(f"Points: {sum(map(lambda x: 0 if not x[1] else pow(2, x[1] - 1), cards))}")
    print(f"Number of cards: {number_of_cards}")
