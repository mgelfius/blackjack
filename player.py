import random

class Player(object):
    hand = []
    handValue = 0
    printTop = '_______'
    printBottom = '|_____|'
    printBlank = '|     |'
    printSpace = '   '

    def printHand(self):
        print(self.name + ': ')
        print(self.printTop + self.printSpace + self.printTop)
        print('|  ' + self.hand[0].displaySuit + '  |' + self.printSpace + '|  ' + self.hand[1].displaySuit + '  |')
        print('|' + self.hand[0].displayValue + '|' + self.printSpace + '|' + self.hand[1].displayValue + '|')
        print(self.printBlank + self.printSpace + self.printBlank)
        print(self.printBottom + self.printSpace + self.printBottom)
        print('Points: ' + str(self.handValue))
        print()

    def __init__(self, cards, number, handValue):     
        self.hand = cards
        self.handValue = handValue
        if number == 0:
            self.name = 'Dealer'
        else:
            self.name = 'Player ' + str(number)
    
def makePlayer(deck, number):
    random.seed(a = None)
    cards = []
    firstCardIndex = random.randrange(0, len(deck.cardsLeft))
    firstCard = deck.cardsLeft[firstCardIndex]
    del deck.cardsLeft[firstCardIndex]
    cards.append(firstCard)

    secondCardIndex = random.randrange(0, len(deck.cardsLeft))
    secondCard = deck.cardsLeft[secondCardIndex]
    del deck.cardsLeft[secondCardIndex]
    cards.append(secondCard)

    handValue = firstCard.points + secondCard.points

    return Player(cards, number, handValue)