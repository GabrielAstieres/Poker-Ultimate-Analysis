# Find a straight flush in the cards.
# Param Expects array of cards.
# Returns 0 if there is no Straight flush.
# Returns The sum of the values of the card making the straight flush.
def isStraightFlush(cards):
    hearts = [number for (color,number) in cards if color == 'H']
    clubs = [number for (color,number) in cards if color == 'C']
    diamonds = [number for (color,number) in cards if color == 'D']
    spades = [number for (color,number) in cards if color == 'S']
    color = max([hearts, clubs, diamonds, spades], key = lambda i: len(i))

    if(len(color)<5):return 0

    color = sorted(set(color))
    followingCards = [color.pop(0)]
    while(color):
        next = color.pop(0)
        if(followingCards[-1] == next -1): followingCards += [next]
        else: 
            if(len(followingCards)<5):
                followingCards = [next]
            else: break

    if(len(followingCards)<5):return 0
    return sum(followingCards[-5:])
    

# Find a flush in the cards, doesn't consider straight flush.
# Param Expects array of cards.
# Returns 0 if there is no flush.
# Returns The sum of the values of the card making the flush.
def isFlush(cards):
    cards.sort(key=lambda cards: cards[1])
    hearts = [number for (color,number) in cards if color == 'H']
    clubs = [number for (color,number) in cards if color == 'C']
    diamonds = [number for (color,number) in cards if color == 'D']
    spades = [number for (color,number) in cards if color == 'S']
    color = max([hearts, clubs, diamonds, spades], key = lambda i: len(i))
    
    if(len(color)<5):return 0
    
    return sum(color[-5:])


# Find the strongest straight in the cards, if any.
# Param Expects array of cards.
# Returns 0 if there is no straight.
# Returns The sum of the values of the card making the straight.
def isStraight(cards):
    cards = [card[1] for card in cards]
    cards = sorted(set(cards))

    followingCards = [cards.pop(0)]
    while(cards):
        next = cards.pop(0)
        if(followingCards[-1] == next -1): followingCards += [next]
        else: 
            if(len(followingCards)<5):
                followingCards = [next]
            else: break
    
    if(len(followingCards)<5):return 0
    
    return sum(followingCards[-5:])



# Find if there is a four of a kind.
# Param Expects array of cards.
# Returns The value of the four of a kind and the additional high card.
def isFourOfAkind(cards):
    cards = [card[1] for card in cards]
    values = set(cards)
    fourOfAkind = 0

    for value in values:
        if(cards.count(value) == 4):
            fourOfAkind = value
            break

    if(fourOfAkind):
        values.remove(fourOfAkind)
        highCard = max(values)
        return fourOfAkind, highCard
    
    return 0


# Find if there is a three of a kind.
# Param Expects array of cards.
# Returns The value of the three of a kind and the sum of the two high cards.
def isThreeOfAkind(cards):
    cards = [card[1] for card in cards]
    values = sorted(set(cards), reverse=1)
    threeOfAkind = 0

    for value in values:
        if(cards.count(value) == 3):
            threeOfAkind = value
            break

    if(threeOfAkind):
        values.remove(threeOfAkind)
        firstHighCard = max(values)

        values.remove(firstHighCard)
        secondHighCard = max(values)
        return threeOfAkind, firstHighCard + secondHighCard

    return 0


# Find if there is a double pair.
# Param Expects array of cards.
# Returns The values of the double pair and then the high card
# 0 if no double pair
def isDoublePair(cards):
    cards = [card[1] for card in cards]
    values = sorted(set(cards), reverse=1)

    pair = 0
    for value in values:
        if(cards.count(value) == 2):
            pair = value
            break
    
    if(pair == 0): return 0
    values.remove(pair)

    secondPair = 0
    for value in values:
        if(cards.count(value) == 2):
            secondPair = value
            break

    if(secondPair != 0):
        values.remove(secondPair)
        return pair, secondPair, max(values)
    
    return 0 
    
    
# Find if there is a there is a pair.
# Param Expects array of cards.
# Returns The value of the pair and the sum of the three high cards.
# 0 if no pair
def isPair(cards):
    cards.sort(key=lambda cards: cards[1])
    cards = [card[1] for card in cards]
    values = sorted(set(cards), reverse=1)

    pair = 0
    for value in values:
        if(cards.count(value) > 1):
            pair = value
            break

    if(pair):
        values.remove(pair)
        return pair, sum(values[0:3])
    return 0

# Find if there is a Full House.
# Param Expects array of cards.
# Returns The value of the three of a kind and the value of the pair.
def isFullHouse(cards):
    threeOfAkind = isThreeOfAkind(cards)
    if(threeOfAkind == 0): return 0

    cards = [card[1] for card in cards]
    values = sorted(set(cards), reverse=1)
    values.remove(threeOfAkind[0])

    pair = 0
    for value in values:
        if(cards.count(value) > 1):
            pair = value
            break

    if(pair == 0): return 0

    return threeOfAkind[0], pair

# Returns the value of the five high cards of a hand.
def getHighCardsValues(cards):
    cards.sort(key=lambda cards: cards[1])
    cards = [card[1] for card in cards]
    values = sorted(cards, reverse=1)[0:5]
    return(sum(values))