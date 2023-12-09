from pathlib import Path
from collections import Counter

card_strength = {'A': (14, 14),
                 'K': (13, 13),
                 'Q': (12, 12),
                 'J': (11, 1),
                 'T': (10, 10),
                 '9': (9, 9),
                 '8': (8, 8),
                 '7': (7, 7),
                 '6': (6, 6),
                 '5': (5, 5),
                 '4': (4, 4),
                 '3': (3, 3),
                 '2': (2, 2)}

class Hand():
    def __init__(self, content, bid, j_is_special = 0):
        self.content = content
        self.j_is_special = j_is_special
        count = Counter(content)
        keys, self.type = [list(x) for x in zip(*sorted(count.items(), key= lambda x: x[1], reverse=True))]
        if j_is_special:
            try: 
                idx = keys.index('J')
                if len(self.type) > 1:
                    if idx:
                        self.type[0] += self.type[idx]
                    else:
                        self.type[1] += self.type[idx]
                    del self.type[idx]
            except ValueError:
                pass
        self.bid = bid

    def __lt__(self, other):
        if self.type == other.type:
            for i,c in enumerate(self.content):
                if card_strength[c][self.j_is_special] < card_strength[other.content[i]][self.j_is_special]:
                    return True
                elif card_strength[c][self.j_is_special] > card_strength[other.content[i]][self.j_is_special]:
                    break
            return False
        return self.type < other.type


with open(Path(__file__).parent / "data") as file:
    hands_unpacked = [(hand, int(bid)) for hand,bid in [line.rstrip('\n').split() for line in file.readlines()]]
    hands = [Hand(hand[0],hand[1]) for hand in hands_unpacked]
    hands.sort()
    hands_special_j = [Hand(hand[0],hand[1],j_is_special=1) for hand in hands_unpacked]
    hands_special_j.sort()

print(f"Winnings: {sum([rank * hand.bid for rank, hand in enumerate(hands, start=1)])}")
print(f"Winnings with special J: {sum([rank * hand.bid for rank, hand in enumerate(hands_special_j, start=1)])}")
    
