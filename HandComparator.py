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
        if(straightFlush[-1] == 14): return 10, straightFlush
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

