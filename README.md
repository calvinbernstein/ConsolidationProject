# tupleOut: *a game by Calvin Bernstein*

**tupleOut is a simple dice game designed for multiple players (two for this version). The program will walk players through the game and prompt them to make choices. When the game is over, tupleOut will create a "results" file or append to an existing one with the results of the game.**

### How It Works:
- The object of the game is to score the most points, or to be the first to reach a certain score.
- Players take turns rolling dice to score points, as described below.
- Each turn, the active player rolls three dice:
	- If all three dice are rolled with the same number, the player has “tupled out”, and ends their turn with zero points. (For example, rolling three “4”s at the same time.)
	- If two dice have the same value, they are “fixed”, and they cannot be re-rolled.
	- During their turn, the player can re-roll any dice that are not “fixed”, as often as they would like, until they decide to stop, or until they “tuple out” (get three of the same number).
- When a player decides to stop, they score points equal to the total of the three dice, and then
their turn ends.
- If a player “tuples out”, their turn ends and they score 0 points for that turn.

### Example Scenarios
1. A player starts out by rolling a 1, 2, and 2 on three dice.
	- The 2’s are fixed, because there’s two of them, so they can’t re-roll those.
	- But they want to reroll the 1, since it’s so low.
	- They re-roll it to a 3, but they want to re-roll it again, to try to get higher.
	- When they re-roll the second time, it turns up as a 2, and since the other two dice are also 2’s, they have “tupled out”. They get zero points for the round.

2. A player starts by rolling a 1, 2, and 4.
	- They decide to roll all three again, and they get a 1 and two 5’s. This means the two 5’s are fixed, and they could choose to re-roll the 1.
	- However, they decide to stop here, because the 5’s are high, and they don’t want to risk “tupling out” by re-rolling the 1 and getting a third 5.
	- So they stop their turn with 11 points (5 + 5 + 1).


### Additional Questions and Future Plans

**When is the game over?**
The game ends after five rounds.

**How and when will you display the running scores, so that players know what the current scores are?**
The scores will be displayed after each round.
    

**Can the game record the scores for each game, including who won?**
The game will record the scores for each game at the end, including the final scores and the winner between the players.

**Can the game record something like “high score” records over many games, or a running tally of how many games a particular player has won?**
This feature will be added in a future version of the game, probably by storing the data in a CSV file.

**Would the game be better or more interesting if the dice were changed, including the number of dice or the number of values on each die?**
The program has been designed with customization in mind. Many functions can be easily modified to change the number of dice rolled, the number of values on each die, and the values themselves.

**What about adding rules for additional special scoring?**
There are currently no plans for additional special scoring, but it may be added in a future version.

**How do I start the game?**
Place the python file in a directory where you are comfortable with a results file being created. From there, navigate to the directory in your terminal and run the program using `python tupleOut.py`. Everything is straightforward after that!
	