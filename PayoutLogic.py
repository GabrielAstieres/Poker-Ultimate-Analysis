# Finds how much was gained or lost in the last round.
# Param Expects amount of the ante.
# Param Expects the amount bet by the player.
# Param Expects the amount of the trips.
# Param Expects the value returned by `getWinner`.
# Returns The amount.
def getBalanceVariation(anteAmount, playedAmount, tripsAmount, hand):
    variation = 0

    if(hand[1] > 3): variation += payTrips(tripsAmount, hand[1])
    else: variation -= tripsAmount

    if(hand[0] == 1):
        if(hand[1] > 4): variation += payAnte(anteAmount, hand[1])
        variation += playedAmount
        variation += anteAmount

    if(hand[0] == 2):
        variation -= playedAmount 
        variation -= 2 * anteAmount
        
    return variation

# Pays Bonus according to the trips and hand combination.
# Param Expects the amount of the trips.
# Param Expects strenght of the hand of the player.
# Returns amount.
def payTrips(tripsAmount, handCombination):
    if(handCombination ==10): return 50 * tripsAmount
    if(handCombination == 9): return 40 * tripsAmount
    if(handCombination == 8): return 30 * tripsAmount
    if(handCombination == 7): return 8 * tripsAmount
    if(handCombination == 6): return 6 * tripsAmount
    if(handCombination == 5): return 5 * tripsAmount    
    if(handCombination == 4): return 3 * tripsAmount

# Pays Blinds according to the ante and hand combination.
# Param Expects the amount of the ante.
# Param Expects strenght of the hand of the player.
# Returns amount.
def payAnte(anteAmount, handCombination):
    if(handCombination == 10): return 500 * anteAmount
    if(handCombination == 9): return 50 * anteAmount
    if(handCombination == 8): return 10 * anteAmount
    if(handCombination == 7): return 3 * anteAmount
    if(handCombination == 6): return (3/2) * anteAmount
    if(handCombination == 5): return anteAmount    