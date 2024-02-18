class Card():
    def __init__(self, suit, value):   
        self.suit = suit
        self.value = value
        self.displaySuit = getDisplaySuit(self) 
        self.displayValue = getDisplayValue(self)
        self.points = getPoints(self)       

def buildCard(suit, value):
    return Card(suit, value)

def getDisplaySuit(self):
    if self.suit == 'Hearts':
        return '♥'
    if self.suit == 'Diamonds':
        return '♦'
    if self.suit == 'Clubs':
        return '♣'
    if self.suit == 'Spades':
        return '♠'

def getDisplayValue(self):
    if self.value == '10':
        return '  ' + self.value + ' '
    else:
        return '  ' + self.value[0] + '  '

def getPoints(self):
    if self.value == 'Ace':
        return 11
    if self.value == 'King' or self.value == 'Queen' or self.value == 'Jack':
        return 10
    else:
        return int(self.value)