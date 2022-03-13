import HandReader
import copy


# Return the hand value according to this table:
# 10: Royal Straight Flush
# 9: Straight Flush
# 8: Quads
# 7: Full house
# 6: Flush
# 5: Straight
# 4: Three of a Kind
# 3: Two pairs
# 2: Pair 
# 1: High card
def getHandValue(cards):
    straightFlush = HandReader.isStraightFlush(copy.deepcopy(cards))
    if(straightFlush != 0):
        if(straightFlush == 60): return 10, straightFlush
        else: return 9, straightFlush

    quads = HandReader.isFourOfAkind(copy.deepcopy(cards))
    if(quads !=0): return 8, quads

    fullHouse = HandReader.isFullHouse(copy.deepcopy(cards))
    if(fullHouse != 0): return 7, fullHouse

    flush = HandReader.isFlush(copy.deepcopy(cards))
    if(flush != 0): return 6, flush

    straight = HandReader.isStraight(cards)
    if(straight !=0): return 5, straight

    threeOfAKind = HandReader.isThreeOfAkind(copy.deepcopy(cards))
    if(threeOfAKind != 0): return 4, threeOfAKind

    doublePair = HandReader.isDoublePair(copy.deepcopy(cards))
    if(doublePair != 0): return 3, doublePair

    pair = HandReader.isPair(copy.deepcopy(cards))
    if(pair != 0): return 2, pair
    
    highCardsValues = HandReader.getHighCardsValues(cards)
    return 1, highCardsValues


# Finds who won the round.
# Returns 1 if the player won, 2 if the dealer won, 0 if tide.
# Returns The hand of the player for bonus calculation.
def getWinner(flop, river, dealer, player):
    dealerHand = getHandValue(flop + river + player)
    playerHand = getHandValue(flop + river + dealer)

    if(playerHand[0] > dealerHand[0]): return 1, playerHand[0]
    if(dealerHand[0] > playerHand[0]): return 2, playerHand[0]
    return compareHand(playerHand[1], dealerHand[1]), playerHand[0]


# Compare two hands that have the same combination.
# Returns 1 if the player won, 2 if the dealer won, 0 if tide.
def compareHand(handPlayer, handDealer):
    while(handPlayer):
        playerScore = handPlayer.pop(0)
        dealerScore = handDealer.pop(0)
        
        if(playerScore > dealerScore): return 1
        if(dealerScore > playerScore): return 2
    return 0