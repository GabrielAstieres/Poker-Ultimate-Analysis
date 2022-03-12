
# Find a flush in the cards, doesn't consider straight flush.
# Param Expects array of cards.
# Returns Empty list if there is no flush.
# Returns The cards forming the highest flush otherwise.
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


# Find the strongest straight in the cards, if any.
# Param Expects array of cards.
# Returns Empty list if there is no straight.
# Returns The cards of the straight, boolean indicating straight Flush.
def isStraight(cards):
    cards.sort(key=lambda cards: cards[1])
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