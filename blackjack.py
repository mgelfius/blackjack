import deck
import player

def main():
    print("How many decks?")
    numberOfDecks = int(input())
    print("How many players?")
    numberOfPlayers = int(input())

    currentDeck = deck.makeDecks(numberOfDecks)
    players = deal(currentDeck, numberOfPlayers)
    

def deal(deck, numberOfPlayers):
    players = []
    for playerNumber in range(numberOfPlayers):
        players.append(player.makePlayer(deck, playerNumber))
    return players

if __name__ == "__main__":
    main()