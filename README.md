# Jacob Hajjar's Verion of the Pig Game

## Synopsis and Rules
I've written my version of the Pig game which can be played in the terminal using python. The rules are that 2-4 players must each take turns. In their turns, they will have the option to roll a dice or hold. If they roll the dice and it does not land on a 1, they will gain a the dice's number of points in that turn. If they roll a 1, they will recieve no points for that turn. The player can keep rolling as many times as they want during their turn, but will lose all of the points they have accumulated if they roll a 1. If the player never rolls a 1, before any roll they can decide to hold the number of points they have earned in their turn and it will be added to their total points. The first player to reach 100 points wins the game. 

# Gameplay Example
There are two players. 

Player 1's Turn:
Player 1 decides to roll the dice and gets a 5. Turn Points: 5  Total Points: 5
Plater 1 rolls a 1. Turn Points: 5  Total Points: 5
They earn no points.

Player 2's Turn:
Decides to roll
Player 2 rolls a 3. Turn Points: 3  Total Points: 3
Player 2 rolls a 4. Turn points: 7  Total Points: 7
Player 2 Holds. Total Points: 7

Player 1's Turn
Decides to roll
Player 1 rolls a 6. Turn Points: 6  Total Points: 6
Player 1 Holds. Total Points: 6

Player 2's turn
Decides to roll
Player 2 rolls a 1. Turn Points: 0  Total Points: 7

This pattern continues until one player reaches 100 points.

# Special Features
My version of the game features a moderate difficulty computer to play against if 1 player mode is selected. The game also has a hot seat feature, where 2-4 players can take turns playing with eachother. Another special features of my Pig game are special phrases added to your roll which tells you if you had an especially lucky roll of the dice.
