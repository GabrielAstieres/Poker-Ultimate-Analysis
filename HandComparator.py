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

    if(dealerHand[0] == playerHand[0]):
        if(playerHand[0] == 10): return 0, 10

        if(playerHand[0] == 9): 
            if(dealerHand[1] > playerHand[1]): return 2, 9
            if(playerHand[1] > dealerHand[1]): return 1, 9
            return 0, 9
        
        if(playerHand[0] == 8): 
            if(dealerHand[1][0] > playerHand[1][0]): return 2, 8
            if(playerHand[1][0] > dealerHand[1][0]): return 1, 8
            if(dealerHand[1][1] > playerHand[1][1]): return 2, 8
            if(playerHand[1][1] > dealerHand[1][1]): return 1, 8
            return 0,8

        if(playerHand[0] == 7): 
            if(dealerHand[1][0] > playerHand[1][0]): return 2, 7
            if(playerHand[1][0] > dealerHand[1][0]): return 1, 7
            if(dealerHand[1][1] > playerHand[1][1]): return 2, 7
            if(playerHand[1][1] > dealerHand[1][1]): return 1, 7
            return 0,7

        if(playerHand[0] == 6): 
            if(dealerHand[1] > playerHand[1]): return 2, 6
            if(playerHand[1] > dealerHand[1]): return 1, 6
            return 0,6

        if(playerHand[0] == 5): 
            if(dealerHand[1] > playerHand[1]): return 2, 5
            if(playerHand[1] > dealerHand[1]): return 1, 5
            return 0,5

        if(playerHand[0] == 4): 
            if(dealerHand[1][0] > playerHand[1][0]): return 2, 4
            if(playerHand[1][0] > dealerHand[1][0]): return 1, 4
            if(dealerHand[1][1] > playerHand[1][1]): return 2, 4
            if(playerHand[1][1] > dealerHand[1][1]): return 1, 4
            return 0,4

        if(playerHand[0] == 3): 
            if(dealerHand[1][0] > playerHand[1][0]): return 2, 3
            if(playerHand[1][0] > dealerHand[1][0]): return 1, 3
            if(dealerHand[1][1] > playerHand[1][1]): return 2, 3
            if(playerHand[1][1] > dealerHand[1][1]): return 1, 3
            if(dealerHand[1][2] > playerHand[1][2]): return 2, 3
            if(playerHand[1][2] > dealerHand[1][2]): return 1, 3
            return 0,3
            

        if(playerHand[0] == 2): 
            if(dealerHand[1][0] > playerHand[1][0]): return 2, 2
            if(playerHand[1][0] > dealerHand[1][0]): return 1, 2
            if(dealerHand[1][1] > playerHand[1][1]): return 2, 2
            if(playerHand[1][1] > dealerHand[1][1]): return 1, 2
            return 0,2

        if(playerHand[0] == 1): 
            if(dealerHand[1] > playerHand[1]): return 2, 1
            if(playerHand[1] > dealerHand[1]): return 1, 1
            return 0,1
