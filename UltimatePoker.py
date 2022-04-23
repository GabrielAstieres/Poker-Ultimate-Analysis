from PayoutLogic import getBalanceVariation
from PlayerStrategy import getBetSize
from HandComparator import getWinner
import matplotlib.pyplot as plt
import random

# Create a standard 52 card deck.
# Cards are tuples (color, value).
# C, H, D, S stands for Clubs, Hearts, Diamonds, Spades.
# 11, 12, 13, 14 are representing Jack, Queen, King & Ace.
def createDeck():
    deck = [('C', 2), ('C', 3), ('C', 4), ('C', 5), ('C', 6), ('C', 7), ('C', 8), ('C', 9), ('C', 10), ('C', 11), ('C', 12), ('C', 13), ('C', 14), 
            ('H', 2), ('H', 3), ('H', 4), ('H', 5), ('H', 6), ('H', 7), ('H', 8), ('H', 9), ('H', 10), ('H', 11), ('H', 12), ('H', 13), ('H', 14), 
            ('D', 2), ('D', 3), ('D', 4), ('D', 5), ('D', 6), ('D', 7), ('D', 8), ('D', 9), ('D', 10), ('D', 11), ('D', 12), ('D', 13), ('D', 14), 
            ('S', 2), ('S', 3), ('S', 4), ('S', 5), ('S', 6), ('S', 7), ('S', 8), ('S', 9), ('S', 10), ('S', 11), ('S', 12), ('S', 13), ('S', 14)]
    random.shuffle(deck)
    return(deck)

# Draws desired number of cards from a deck.
# Param Expects a deck of cards.
# Param Expects the number of desired cards.
# Returns The array of cards, made of tuples (color, value).
def getCard(deck, nb):
    cards = []
    for i in range(nb):
        cards.append(deck.pop())
    return cards

# Creates a board, a hand for the dealer, a hand for the player.
# @dev: because this is Ultimate poker, there is no distinction between turn & river.
def setRound():
    deck = createDeck()
    flop = getCard(deck, 3)
    river = getCard(deck, 2)
    player = getCard(deck, 2)
    dealer = getCard(deck, 2)
    return(flop, river, dealer, player) 

    
def main():
    rounds = range(10000) # Number of round to play.
    balance = [10000] # Initial balance when starting the game.
    anteAmount = 1 # Amount bet on the Ante.
    tripsAmount = 2 # Amount bet on the Trips.
    lost = won = 0
    
    for round in rounds[:-1]:
        if(balance[-1] > 0):
            # Recreate a fresh round each time.
            (flop, river, dealer, player) = setRound() 
            
            # Get amount played according to the strategy.
            playedAmount = getBetSize(flop, river, player, anteAmount) 

            # If player didn't bet at all, round is lost.
            if(playedAmount == 0): 
                balance.append(balance[-1] - tripsAmount - 2*anteAmount)
                lost += 1
                continue
            
            # Get the winner of the round.
            results = getWinner(flop, river, dealer, player) 

            if(results[0] == 1): won += 1
            else: lost+=1

            # Get the balance variation.
            variation = getBalanceVariation(anteAmount, playedAmount, tripsAmount, results) 
            balance.append(balance[-1] + variation)

        else: balance.append(0)

    plt.plot(rounds, balance)
    plt.xlabel("Number of rounds")
    plt.ylabel("Player's balance")    
    plt.show()

if __name__ == "__main__":
    main()
