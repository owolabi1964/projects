import doctest # To confirm that Card(2, 12) will display as 'Queen of Hearts'.
class Card:
    """
    Create class Card:
    There are fifty-two cards in a deck, \
    each of which belongs to one of four suits \
    and one of thirteen ranks. \
    The suits are Spades, Hearts, Diamonds, and Clubs. \
    The ranks are Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, and King.
    """
    SUITS = (['Clubs', 'Diamonds', 'Hearts', 'Spades'])
    RANKS = (['start', 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', \
        'Jack', 'Queen', 'King'])

    def __init__(self, suit=0, rank=0):
        """Constructor for the card instances"""
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """
        Used the str function. Passing an object \
        as an argument to str is equivalent to \
        invoking the __str__ method on the object.\
          >>> print(Card(2, 12)) 
          Queen of Hearts
        """
        return '{0} of {1}'.format(Card.RANKS[self.rank], Card.SUITS[self.suit])
    def show_card(self):
        """Show Card."""
if __name__ == '__main__':
    doctest.testmod()
    # unittest.main()

class Deck:
    """Deck Section"""
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))


    def print_deck(self):
        """Print the Deck of Cards"""
        for card in self.cards:
            print(card)

    def __str__(self):
        """
        Used the str function. Passing an object \
        as an argument to str is equivalent to \
        invoking the __str__ method on the object.
        """
        string_accumulator = ""
        for i in range(len(self.cards)):
            string_accumulator += " " * i + str(self.cards[i]) + "\n"
        return string_accumulator
    def remove(self, card):
        """
        Removes card from the deck, which takes a card as a parameter. \
        It removes it, and returns True if the card was in the deck and False otherwise
        """
        if card in self.cards:
            self.cards.remove(card)
            return True
        else:
            return False

    def pop(self):
        """
        Pop removes the last card in the list, \
        from the bottom of the deck.
        """
        return self.cards.pop()

    def is_empty(self):
        """
        Boolean function 'is_empty', which returns true if the deck \
        contains no cards
        """
        return len(self.cards) == 0
