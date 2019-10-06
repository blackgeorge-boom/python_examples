import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:

    ranks = [str(n) for n in range(2, 11)] + list('KQJA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks
                                        for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    print(card)
    print(rank_value)
    return rank_value * len(suit_values) + suit_values[card.suit]


if __name__ == '__main__':

    beer_card =  Card('A', 'spades')
    print(beer_card)

    deck = FrenchDeck()
    print(len(deck))
    print(deck[-1])

    for card in sorted(deck, key=spades_high):
        print(card)