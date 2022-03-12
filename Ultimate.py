from inspect import getcallargs
from multiprocessing.reduction import duplicate
import random

def createDeck():
    values = range(2,15)*4
    colors = ['C', 'H', 'D', 'S']*14
    deck = [(str(y),int(x)) for y,x in zip(colors, values)]
    return(deck)

deck = createDeck()

def getCard(deck, nb):
    cards = []
    for i in range(nb):
        card = deck[random.randint(0, len(deck)-1)]
        deck.remove(card)
        cards += [card]
    return cards

def isFlush(cards):
    colors = [[],[],[],[]]
    for card in cards:
        if(card[0] == 'H'):colors[0]+=[card]
        if(card[0] == 'C'):colors[1]+=[card]
        if(card[0] == 'S'):colors[2]+=[card]
        if(card[0] == 'D'):colors[3]+=[card]
        
    if(len(colors[0])>4): return sorted(colors[0])[-5:]
    if(len(colors[1])>4): return sorted(colors[1])[-5:]
    if(len(colors[2])>4): return sorted(colors[2])[-5:]
    if(len(colors[3])>4): return sorted(colors[3])[-5:]
    return []


# Find the strongest straight in the cards
# Returns empty list if there is no straight
# Returns the cards of the straight, boolean indicating straight Flush
def isStraight(cards):
    followingValues = [cards[0]]
    for i in range(1,len(cards)):
        if(cards[i][1] == cards[i-1][1]+1 or cards[i][1] == cards[i-1][1]):
            followingValues += [cards[i]]
        else:
            if(len(followingValues) < 5):followingValues = [cards[i]]

    seen = set()
    uniqueValues =  [(a, b) for a, b in followingValues 
         if not (b in seen or seen.add(b))]

    if(len(uniqueValues)>4): 
        flush = isFlush(followingValues)
        if(len(flush)): return flush, True 
        return uniqueValues[-5:], False
    
    return []


for i in range(1):
    
    #cards = getCard(createDeck(),7)
    cards = [('H', 2), ('C', 9), ('C', 10), ('C', 11), ('D', 12), ('S', 12), ('H', 12) ,('C', 13)]
    cards.sort(key=lambda cards: cards[1])
    print(cards)
    print(isStraight(cards))
    print('')

# board = getCard(deck, 5)
# player = getCard(deck, 2) + board
# dealer = getCard(deck, 2) + board
# player.sort(key=lambda player: player[1])
# dealer.sort(key=lambda dealer: dealer[1])