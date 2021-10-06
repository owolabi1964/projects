import random
class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self):
        print(f"{self.value} of {self.suit}")

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Clubs", "Diamonds", "Hearts", "Spades"]:
            for v in range(1,14):
                self.cards.append(Card(s, v))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
            

    def draw(self):
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.draw())
        return self

    def showHand(self):
        for card in self.hand:
            card.show()

    def winning_value(self):
        for s in ["Clubs", "Diamonds", "Hearts", "Spades"]:
            if s == "Clubs":
                value1 = 4
            elif
                s == "Diamonds":
                value2 = 3
            elif
                s == "Hearts":
                value3 = 2
            elif 
                s == "Spades"
                value4 = 1

            # return self.hand.pop()

# card = Card("Clubs", 2)
# card.show()

deck = Deck()
deck.shuffle()
# deck.show()
print(f"1st Player")
bob = Player("Bob")
bob.draw(deck).draw(deck).draw(deck)
bob.showHand()
print(f"\n2nd Player")
frank = Player("Frank")
frank.draw(deck).draw(deck).draw(deck)
frank.showHand()
print(frank.winning_value())

# card = deck.draw()
# card.show()