from HandComparator import getHandValue
import HandReader
import copy

# Finds The amount the player decides to bet on this hand.
# Param Expects cards of the flop (3 cards).
# Param Expects cards of the river (2 cards).
# Param Expects cards of the player (2 cards).
# Param Expects anteAmount, the amount put on the ante.
# Returns Bet amount.
def getBetSize(flop, river, player, anteAmount):
    if(doBetPreFlop(copy.deepcopy(player))): return 4 * anteAmount
    if(doBetFlop(player, flop)): return 2 * anteAmount
    # if(doBetRiver(player, flop + river)): return anteAmount
    return 1

# Finds If the bets Pre flop.
# Param Expects cards of the player (2 cards).
# Returns Boolean, if bet.
def doBetPreFlop(player):
    if(HandReader.isPair(player) != 0): return True
    return False

# Finds If the bets Post flop.
# Param Expects cards of the player (2 cards).
# Returns Boolean, if bet.
def doBetFlop(player, flop):
    flopStrength = getHandValue(flop)
    playerStrength = getHandValue(flop + player)
    if(playerStrength[0] > flopStrength[0]): return True
    return False

# Finds If the bets On river.
# Param Expects cards of the player (2 cards).
# Returns Boolean, if bet.
def doBetRiver(player, board):
    playerStrength = getHandValue(player + board)
    boardStrength = getHandValue(board)
    
    if(playerStrength[0] > 1 and playerStrength[0] != boardStrength[0]): return True
    return False 