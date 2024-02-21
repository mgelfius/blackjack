import deck
import player
import random
import time

def main():
    print("How many decks?")
    numberOfDecks = int(input())
    print("How many players?")
    numberOfPlayers = int(input())
    continuePlay = True

    while continuePlay:
        currentDeck = deck.makeDecks(numberOfDecks)
        players = deal(currentDeck, numberOfPlayers)
        gameplay(currentDeck, players)
        continuePlay = playAgain()

def deal(deck, numberOfPlayers):
    players = []
    for playerNumber in range(numberOfPlayers + 1):
        players.append(player.makePlayer(deck, playerNumber))
    return players

def gameplay(deck, players):
    for play in players:
        play.printHand(True)
        time.sleep(1)
    anyActivePlayers = True
    while anyActivePlayers:
        for activePlayer in players:
            if activePlayer.name != 'Dealer':
                canContinue = True
                while canContinue and getAction(activePlayer):
                    hit(deck, activePlayer)
                    activePlayer.printHand(True)
                    time.sleep(1)
                    if activePlayer.handValue > 21:
                        canContinue = False
                        print(activePlayer.name + ' busts')
                        time.sleep(1)
                    elif activePlayer.handValue == 21:
                        canContinue = False
                stand(activePlayer)
        anyActivePlayers = isAnyActivePlayers(players)
    dealerTurn(players[0], deck)
    scoring(players)

def scoring(players):
    endValue = ''
    dealerHand = players[0].handValue
    if dealerHand <= 21:
        for play in players:
            if play.name != 'Dealer': 
                if play.handValue > 21:
                    endValue = ' loses'
                elif play.handValue > players[0].handValue:
                    endValue = ' wins'
                elif play.handValue == players[0].handValue:
                    endValue = ': push'
                else:
                    endValue = ' loses'
                print(play.name + endValue)
                time.sleep(1)
    else:
        for play in players:
            if play.name != 'Dealer':
                if play.handValue > 21:
                    endValue = ' loses'
                else:
                    endValue = ' wins'
                print(play.name + endValue)
                time.sleep(1)

def dealerTurn(dealer, currentDeck):
    dealer.printHand(False)
    canContinue = dealer.handValue < 17
    while canContinue:
        hit(currentDeck, dealer)
        dealer.printHand(False)
        time.sleep(1)
        if dealer.handValue >= 17:
            canContinue = False
        if dealer.handValue > 21:
            print(dealer.name + ' busts')
            time.sleep(1)

def getAction(activePlayer):
    validInput = False
    inputValue = ''
    while not validInput:
        activePlayer.printHand(False)
        print(activePlayer.name + ': [H]it or [S]tand')
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

def playAgain():
    validInput = False
    inputValue = ''
    while not validInput:
        print('Play again? [Y]es or [N]o')
        inputValue = input().lower()
        if inputValue == 'y' or inputValue == 'n':
            validInput = True
    if inputValue == 'y':
        return True
    else:
        return False

if __name__ == "__main__":
    main()