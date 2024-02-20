import deck
import player
import random

def main():
    print("How many decks?")
    numberOfDecks = int(input())
    print("How many players?")
    numberOfPlayers = int(input())

    currentDeck = deck.makeDecks(numberOfDecks)
    players = deal(currentDeck, numberOfPlayers)
    
    gameplay(currentDeck, players)

def deal(deck, numberOfPlayers):
    players = []
    for playerNumber in range(numberOfPlayers + 1):
        players.append(player.makePlayer(deck, playerNumber))
    return players

def gameplay(deck, players):
    for play in players:
        play.printHand()
    anyActivePlayers = True
    while anyActivePlayers:
        for activePlayer in players:
            if activePlayer.name != 'Dealer':
                canContinue = True
                while canContinue and getAction(activePlayer.name):
                    hit(deck, activePlayer)
                    activePlayer.printHand()
                    if activePlayer.handValue >= 21:
                        canContinue = False
                stand(activePlayer)
        anyActivePlayers = isAnyActivePlayers(players)

def getAction(playerName):
    validInput = False
    inputValue = ''
    while not validInput:
        print(playerName + ': [H]it or [S]tand')
        inputValue = input().lower()
        if inputValue == 'h' or inputValue == 's':
            validInput = True
    if inputValue == 'h':
        return True
    else:
        return False

def hit(deck, currentPlayer):
    cardIndex = random.randrange(0, len(deck.cardsLeft))
    newCard = deck.cardsLeft[cardIndex]
    del deck.cardsLeft[cardIndex]
    currentPlayer.drawCard(newCard)

def stand(currentPlayer):
    currentPlayer.isOut = True

def isAnyActivePlayers(players):
    outPlayerCount = 1
    for play in players:
        if play.isOut == True:
            outPlayerCount = outPlayerCount + 1
    if outPlayerCount == len(players):
        return False
    else:
        return True

if __name__ == "__main__":
    main()