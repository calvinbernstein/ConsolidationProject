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
    "playerOneDice": [3, 3],    # List for storing Player One's matching dice
    "playerOneScore": 0,    # Variable to track Player One's score
    
    "playerTwoID": 2,       # Player ID for Player Two
    "playerTwoDice": [],    # List for storing Player Two's matching dice
    "playerTwoScore": 0,    # Variable to track Player Two's score
    
    "winner": ""
}

# Associate player IDs with names
playerIDs = {
    1: "Player One",
    2: "Player Two"
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
def roundUI(playerID, scoreboard = False):
    
    print(f"************************ ROUND {currentRound} OF {maxRounds} | SCORE: {playerInfo['playerOneScore']}-{playerInfo['playerTwoScore']}")
    
    if currentRound == 1:
        instructions = "Type ROLL to roll the dice.\n"
    elif currentRound > 1:
        instructions = "Type ROLL to roll the dice or PASS to end your turn.\n"
    
    print(playerIDs[playerID] + ", it's your turn. " + instructions)
    
    if playerID == 1:
        if len(playerInfo["playerOneDice"]) > 0:
            print("FIXED DICE: ", playerInfo["playerOneDice"])
    elif playerID == 2:
        if len(playerInfo["playerTwoDice"]) > 0:
            print("FIXED DICE: ", playerInfo["playerTwoDice"])
    
    
    
# Function to check for different scenarios - tuple out, two matching, etc...
"""
checkRoll Function
This function analyzes a list of dice for common scenarios which trigger an event in the game.
More specifically, the function checks for matching dice and "tupling out".

If neither scenarios occur on the roll, the function tells the player how many points they earned and assigns them the points.

If the function finds that the player has "tupled out", it will return the string "tupleOut".
If the function finds any matching dice, it will return a list containing the duplicates.

PARAMETERS:
playerID (required) - Specify which player's roll is being checked.
dice (required) - Input a list of dice to check.
"""
def checkRoll(playerID, dice):
    duplicates = []
        
    if len(dice) > 1:
            
            counter = Counter(dice)
            
            for item, count in counter.items():
                if count > 1:
                    duplicates.extend([item] * count)
                    
            if len(duplicates) > 0:
                
                print("Two of your dice matched. ")
                print(playerInfo["playerOneDice"])
    
    elif len(dice) == 1:
        if playerID == 1:
            # print(playerInfo["playerOneDice"][1])
            if dice == [playerInfo["playerOneDice"][1]]:
                duplicates.extend(dice)
                print("TUPLE OUT")
                
    else:
        raise Exception("checkRoll Error: An improper amount of dice were provided to the function.")
    
    

"""
This variable will keep track of whether the game should continue running or not.
If the maximum number of rounds is reached or a player "tuples out", the gameActive variable will be set to False.
"""
gameActive = True


# Introductory message reminding the user to check the README if they haven't already
print("Welcome to TupleOut! Make sure to read the README for the rules.\n\n")

while gameActive == True:
    currentRound += 1
    
    # Player 1
    roundUI(1)
    playerSelection = input()
    
    if playerSelection == "ROLL":
        currentRoll = diceRoll(diceUsed - len(playerInfo["playerOneDice"]))
        print("Your roll: " + str(currentRoll)+"\n")
            
        # print([playerInfo["playerOneDice"][1]])
        playerInfo["playerOneScore"] += sum(currentRoll)
        checkRoll(1, currentRoll)
    
        

print("GAME OVER **************************************************")

if playerInfo["playerOneScore"] > playerInfo["playerTwoScore"]:
    print(f"Player One won with a final score of ")
    