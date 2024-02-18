import card

class Deck(object):
    cardsLeft = []

    def __init__(self, deckCount):     
        self.cardsLeft = newDeck(deckCount)

def makeDecks(deckCount):
    return Deck(deckCount)

def newDeck(count):
        cards = []
        suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        nonNumericValues = ['Ace', 'Jack', 'Queen', 'King']

        for x in range(count):
            for suit in suits:
                for value in range(2, 11):
                    cards.append(card.buildCard(suit, str(value)))
                for value in nonNumericValues:
                    cards.append(card.buildCard(suit, value))
        return cards