import random

class Player(object):
    hand = []
    handValue = 0
    isOut = False
    printTop = '_______'
    printBottom = '|_____|'
    printBlank = '|     |'
    printSpace = '   '

    def printHand(self, isFirstDeal):
        print(self.name + ': ')

        if self.name == 'Dealer' and isFirstDeal:
            self.printDealerHand()
        else:
            cardTop = ''
            cardSuit = ''
            cardValue = ''
            cardBlankLine = ''
            cardBottom = ''

            for card in self.hand:
                cardTop = cardTop + self.printTop + self.printSpace
                cardSuit = cardSuit + '|  ' + card.displaySuit + '  |' + self.printSpace
                cardValue = cardValue + '|' + card.displayValue + '|' + self.printSpace
                cardBlankLine = cardBlankLine + self.printBlank + self.printSpace
                cardBottom = cardBottom + self.printBottom + self.printSpace
        
            print(cardTop)
            print(cardSuit)
            print(cardValue)
            print(cardBlankLine)
            print(cardBottom)
            print('Points: ' + str(self.handValue))
            print()

    def printDealerHand(self):
        cardTop = ''
        cardSuit = ''
        cardValue = ''
        cardBlankLine = ''
        cardBottom = ''

        cardTop = self.printTop + self.printSpace + self.printTop
        cardSuit = '|  ' + self.hand[0].displaySuit + '  |' + self.printSpace + self.printBlank
        cardValue = '|' + self.hand[0].displayValue + '|' + self.printSpace + self.printBlank
        cardBlankLine = self.printBlank + self.printSpace + self.printBlank
        cardBottom = self.printBottom + self.printSpace + self.printBottom
        
        print(cardTop)
        print(cardSuit)
        print(cardValue)
        print(cardBlankLine)
        print(cardBottom)
        print('Points: ' + str(self.hand[0].points))
        print()

    def calculateHandValue(self):
        handValue = 0
        for card in self.hand:
            handValue = handValue + card.points
        if handValue > 21:
            for card in self.hand:
                if card.points == 11:
                    card.points = 1
                    handValue = handValue - 10
        self.handValue = handValue

    def drawCard(self, card):
        self.hand.append(card)
        self.calculateHandValue()

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
    handValue = 0
    for i in range(2):
        cardIndex = random.randrange(0, len(deck.cardsLeft))
        newCard = deck.cardsLeft[cardIndex]
        del deck.cardsLeft[cardIndex]
        cards.append(newCard)
        handValue = handValue + newCard.points

    return Player(cards, number, handValue)