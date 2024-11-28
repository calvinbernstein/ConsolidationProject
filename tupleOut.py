"""
- Each turn, the active player rolls three dice

- If all three dice are rolled with the same number, the player has “tupled out”, and ends their turn with zero points. (For example, rolling three “4”s at the same time.)

- If two dice have the same value, they are “fixed”, and they cannot be re-rolled.

- During their turn, the player can re-roll any dice that are not “fixed”, as often as they would like, until they decide to stop, or until they “tuple out” (get three of the same number).

- When a player decides to stop, they score points equal to the total of the three dice, and then
"""

import random


# 2 players
# five total turns
# display the scores after each round
# record the scores to a text file
# txt file can store the high scores
# computer player? 
# additional special scoring? different dice?

# Dice roll funciton
def diceRoll(diceQuantity):
    # Options for the sides of the die, can be changed later for special dice
    dieOptions = [1, 2, 3, 4, 5, 6]
    
    diceResults = []
    
    for i in range(0, diceQuantity):
        diceRoll = random.choice(dieOptions)
        diceResults.append(diceRoll)
        
    return diceResults


# /// CONFIGURATION VARIABLES
# Variable for tracking the current round (out of 3)
currentRound = 0

# Maximum rounds for the game
maxRounds = 3

# How many dice are used in the game
diceUsed = 3


# FUNCITON TO RETERN PLAYER'S TURN

# Function to check for different scenarios - tuple out, two matching, etc...
def checkRoll(dice):
    tupleOut = all(i == list[0] for i in list)
    if tupleOut == True:
        return "tupleOut"
    
    # If 3 dice match...
    
# general scorekeeping function - store scores, return the scoreboard, other features
def scorer():
    


print("Welcome to TupleOut! Make sure to read the README for the rules.")
for i in range(0, maxRounds):
    
    
    if currentRound == 0:
        playerSelection = input("PLAYER 1: It's your turn. Type ROLL to roll the dice.")
    elif currentRound > 0:
        playerSelection = input("PLAYER 1: It's your turn. Would you like to ROLL or PASS?")
    
    currentRound += 1
    if playerSelection == "ROLL":
        currentRoll = diceRoll(diceUsed)
        print("Your roll: " + str(currentRoll))
        
        
    
        



