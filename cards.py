import random

class Card(object):
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    # class attributes
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', 
              '8', '9', '10', 'Jack', 'Queen', 'King']
    
    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])


    def __lt__(self, other):
        # checks suits
        card1 = self.suit, self.rank
        card2 = other.suit, other.rank
        return card1 < card2


class Deck(object):
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    # adding methods to add, remove, shuffle, and sort

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

# Inheritance is the ability to define a new class that is a modified
# version of an existsting class.

class Hand(Deck):
    # hand inherits from deck, which means we can use pop_card and add_card
    # if we provide an __init__, it overrides the one from Deck
    def __init__(self, label=''):
        self.cards = []
        self.label = label

# encapsulation

class Markov(object):
    def __init__(self):
        self.suffix_map = {}
        self.prefix = ()

    def process_word(self, word, order=2):
        if len(self.prefix) < order:
            self.prefix += (word,)
            return

        try:
            self.suffix_map[self.prefix].append(word)
        except KeyError:
            # if no entry for prefix, create
            self.suffix_map[self.prefix] = [word]
        self.prefix = shift(self.prefix, word)
    
    

