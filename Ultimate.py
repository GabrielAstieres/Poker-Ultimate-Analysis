from inspect import getcallargs
from multiprocessing.reduction import duplicate
import random
import HandReader



# Create a standard 52 card deck.
# Cards are tuples (color, value).
# C, H, D, S stands for Clubs, Hearts, Diamonds, Spades.
# 11, 12, 13, 14 are representing Jack, Queen, King & Ace.
def createDeck():
    values = range(2,15)*4
    colors = ['C', 'H', 'D', 'S']*14
    deck = [(str(y),int(x)) for y,x in zip(colors, values)]
    return(deck)

# Draws a number of random cards from the deck
def getCard(deck, nb):
    cards = []
    for i in range(nb):
        card = deck[random.randint(0, len(deck)-1)]
        deck.remove(card)
        cards += [card]
    return cards

# Creates a board, a hand for the dealer, a hand for the player
def setRound():
    deck = createDeck()
    flop = getCard(deck, 3)
    river = getCard(deck, 2)
    player = getCard(deck, 2)
    dealer = getCard(deck, 2)
    return(flop, river, dealer, player)
    

def main():
    flop, river, dealer, player = setRound()
    print(HandReader.isThreeOfAkind([('S', 14), ('H', 11), ('H', 11), ('D', 10), ('S', 9), ('C', 11), ('S', 8)]))
    print('')


if __name__ == "__main__":
    main()
