# tupleOut: a game by Calvin Bernstein
# Please see the README file for information on how to play.

# Import required libraries
import random
from collections import Counter

"""
diceRoll Function
For each "roll" (specified by the diceQuantity parameter), the diceRoll function selects a random item from the dieOptions list contained within it and appends the item to a list which is returned after all of the dice have been rolled.

PARAMETERS:
    diceQuantity (optional) - Use this parameter to specify how many dice rolls should be returned. If left blank, the function will roll one die.
"""
def diceRoll(diceQuantity = -1):
    # Options for the sides of the die, can be modified for special dice
    dieOptions = [1, 2, 3, 4, 5, 6]
    
    # List storing dice rolls to be returned
    result = []
    
    if diceQuantity > 0:
        for i in range(0, diceQuantity):
            diceRoll = random.choice(dieOptions)
            result.append(diceRoll)
    elif diceQuantity == -1:
        result.append(random.choice(dieOptions))
    else:
        raise Exception("diceRoll Function Error - A dice roll was called for with an invalid quantity.")
    return result

    
# /// CONFIGURATION VARIABLES
currentRound = 0    # Variable for tracking the current round (out of 3)
maxRounds = 5       # Maximum rounds for the game
diceUsed = 3        # How many dice are rolled for each turn

# Dictionary containing player information
playerInfo = {
    "playerOneID": 1,       # Player ID for Player One
    "playerOneDice": [],    # List for storing Player One's matching dice
    "playerOneScore": 0,    # Variable to track Player One's score
    
    "playerTwoID": 2,       # Player ID for Player Two
    "playerTwoDice": [],    # List for storing Player Two's matching dice
    "playerTwoScore":, 0    # Variable to track Player Two's score
}

# Associate player IDs with names
playerIDs = {
    1, "Player One",
    2, "Player Two"
}

"""
roundUI Function
This function outputs repetitive text including:
    - The game's current round
    - Who's turn it is
    - The current scores of the players

PARAMETERS:
playerID (required) - Specify which player's turn it is using their player ID.
"""
def roundUI(playerID):
    print(f"CURRENT ROUND: {currentRound} | SCORE: {playerInfo['playerOneScore']}-{playerInfo['playerTwoScore']}")

    print(f"{playerIDs[playerID]}, it's your turn.")
    
    if currentRound == 1:
        print("Type ROLL to roll the dice.\n")
    elif currentRound > 1:
        print("PLAYER 1: It's your turn. Would you like to ROLL or PASS?\n")
    
    
# Function to check for different scenarios - tuple out, two matching, etc...
"""
checkRoll Function
This function analyzes a list of dice for common scenarios which trigger an event in the game.
More specifically, the function checks for matching dice and "tupling out".

"""
def checkRoll(dice):
    tupleOut = all(i == list[0] for i in list)
    if tupleOut == True:
        return "tupleOut"
    
    


"""
This variable will keep track of whether the game should continue running or not.
If the maximum number of rounds is reached or a player "tuples out", the gameActive variable will be set to False.
"""
gameActive = True






# Introductory message reminding the user to check the README if they haven't already
print("Welcome to TupleOut! Make sure to read the README for the rules.")

while gameActive == True:
    currentRound += 1
    
    playerSelection = input()
    
    if playerSelection == "ROLL":
        currentRoll = diceRoll(diceUsed)
        print("Your roll: " + str(currentRoll)+"\n")
        
        if len(currentRoll) > 1:
            counter = Counter(currentRoll)
            duplicates = []
            
            for item, count in counter.items():
                if count > 1:
                    duplicates.extend([item] * count)
        
        
        
    
        



