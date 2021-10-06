def sort_card_list():
    """
    Sort cards: Sort cards in ascending order by suit and rank (ace high).
    i.e. If the deck contains cards with the following order:
    (Spades, 2), (Diamonds, 5), (Spades, King), (Hearts, 3), (Clubs, Ace)
    """
    # Deck Sorting program begins here
    deck_list = []
    """
    Empty list created, 'deck_list'.
    """
    deck_list += ('Spades', 2), ('Diamonds', 5), ('Spades', 'King'), ('Hearts', 3), ('Clubs', 'Ace')
    """Used the Anonymous function, Lambda to sort deck."""
    deck_list.sort(key=lambda x: x[0], reverse=True)
    deck_list[2], deck_list[3] = deck_list[3], deck_list[2]
    """
    Swap the order of list.
    """
    # Print the sorted list.
    print(deck_list)

sort_card_list()