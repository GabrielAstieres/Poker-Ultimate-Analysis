import random
import HandComparator

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

# Draws a number of random cards from the deck
def getCard(deck, nb):
    cards = []
    for i in range(nb):
        cards.append(deck.pop())
    return cards

# Creates a board, a hand for the dealer, a hand for the player
def setRound():
    deck = createDeck()
    flop = getCard(deck, 3)
    river = getCard(deck, 2)
    player = getCard(deck, 2)
    dealer = getCard(deck, 2)
    return(flop, river, dealer, player)
    

def printStats(nbOfHands):   
    RSF = SF = Q = FH = F = S = T = PP = P = HC = 0
    for i in range(nbOfHands):
        flop, river, dealer, player = setRound()
        value = HandComparator.getHandValue(flop + river + dealer)
        value = value[0]
        if(value == 10): RSF +=1
        if(value == 9): SF +=1
        if(value == 8): Q +=1
        if(value == 7): FH +=1
        if(value == 6): F +=1
        if(value == 5): S +=1
        if(value == 4): T +=1
        if(value == 3):PP +=1
        if(value == 2): P +=1
        if(value == 1): HC +=1

    print("Royal Straight Flush", RSF)
    print("Straight Flush", SF)
    print("Quads", Q)
    print("Full House", FH)
    print("Flush", F)
    print("Straight", S)
    print("Three of a Kind", T)
    print("Two Pairs", PP)
    print("One Pair", P)
    print("High Card", HC)
    print("Total Number of hands", RSF + SF + Q + FH + F + S + T + PP + P + HC)

    printProba(nbOfHands)
    
def printProba(nbOfHands):
    print("=====================")
    print("RSF", nbOfHands * 0.000032)
    print("SF", nbOfHands * 0.000279)
    print("Quads", nbOfHands * 0.00168)
    print("FH", nbOfHands * 0.026)
    print("Flush", nbOfHands * 0.0303)
    print("Straight", nbOfHands * 0.0462)
    print("Three", nbOfHands * 0.0483)
    print("Two Pairs", nbOfHands * 0.235)
    print("One Pair", nbOfHands * 0.438)
    print("High card", nbOfHands * 0.174)



def main():
    P = D = 0
    for i in range(10000):
        flop, river, dealer, player = setRound()
        w = HandComparator.getWinner(flop, river, dealer, player )
        if(w[0] == 1):
            P += 1
        if(w[0] == 2):
            D += 1
        if(i%1000 == 0): print(str(i/1000) + "%")
    print(P,D)
            

if __name__ == "__main__":
    main()
