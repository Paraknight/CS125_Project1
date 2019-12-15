'''
Created on Jan 27, 2019

@author: Brandon
'''
"""
/* CS 125 - Intro to Computer Science II
 * File Name: CS125_Project1.py
 * Python Programming
 * Project 1 - Due 1/27/2019
 * Instructor: Dr. Dan Grissom
 * 
 * Name 1: Brandon Watanabe
 * Name 2: Natalie Palos
 * Description: Generic description that is different from the skeleton description
 * to help auto-grader testing.
 */
 """

# enum class used to represent each cell of the mine board:
# HM = Hidden Mine, RM = Revealed Mine, HE = Hidden Empty, RE = Revealed Empty
from enum import Enum
class MineCell(Enum):
    HM = 1
    RM = 2
    HE = 3
    RE = 4

# Constants used to make defining the mine board easier
he = MineCell.HE
hm = MineCell.HM

# Definition of mine board. *** DO NOT CHANGE ***
# The hidden mines are represented by 'hm' and the hidden empty
# cells with 'he' in a 5x5 array.
mineBoard = [ [he, he, he, he, he],
    [he, hm, he, hm, he],
    [he, he, he, he, he],
    [he, he, hm, he, he],
    [he, he, hm, hm, he] ];

# For creating new hard-coded test board
"""
mineBoard = [ [hm, hm, hm, hm, hm],
    [he, he, he, he, he],
    [he, he, he, he, he],
    [he, he, he, he, he],
    [he, he, he, he, he] ];
"""

"""
/////////////////////////////////////////////////////////////////////
// This function simply calls your two board printing methods to help
// you test that your print methods are working properly before moving
// on with this lab.
/////////////////////////////////////////////////////////////////////
"""
def testBoardPrinting(board):
    printCurrBoard(board)
    print()
    printGameOverBoard(board);
    print("\n\n*****Exiting program after test. Comment out testBoardPrinting() method in main() to move on.")
    exit()

"""
/////////////////////////////////////////////////////////////////////
// Prints the state of the board while game is still being played:
// '?' for unexplored, 'M' for revealed mines, 'E' for revealed empty cells
/////////////////////////////////////////////////////////////////////
"""
def printCurrBoard(board):
   
    # TODO 1: Write code to print the current game state as specified in the comment above
    
    for i in range(5): #Creating an 2D array with rows and collums
        for j in range(5):
            if (mineBoard[i][j] == MineCell.RE): #If mineboard cell is revealed empty, prints "E"
                print ("E", end = "\t")
            elif (mineBoard[i][j] == MineCell.RM): #If mineboard cell has a revealed mine, prints "M"
                print ("M", end = "\t")
            else: #If mineboard is unexplored, prints '?'
                print ("?", end = "\t")
        print("\n")  #prints an new line after 5 indexes
            
"""
/////////////////////////////////////////////////////////////////////
// Prints the state of the board after the game is over (thus, we can
// reveal everything to the user):
// 'm' for unrevealed mines, 'e' for unrevealed empty cells,
// 'M' for revealed mines, 'E' for revealed empty cells
/////////////////////////////////////////////////////////////////////
"""
def printGameOverBoard(board):
    
    # TODO 2: Write code to print the final (game-over) game state as specified in the comment above
    for i in range(5): ##Creating an 2D array with rows and collums
        for j in range(5):
            if (mineBoard[i][j] == MineCell.RM): #if mineboard cell has a mine that the user revealed, print 'm'
                print ("M", end = "\t")
            elif (mineBoard[i][j] == MineCell.HM): #if mineboard cell has a mine but was never revealed, print 'm'
                print ("m", end = "\t")
            elif (mineBoard[i][j] == MineCell.HE): #if mineboard cell is hidden empty and was never revealed by the user, print 'e'
                print ("e", end = "\t")
            else:
                print ("E", end = "\t") #if mineboard cell was revealed by user and it is empty, print 'E'
        print("\n") #prints an new line after 5 indexes
    

"""
/////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////
// Main method code.
/////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////
"""

# Your program should always output your name and the lab/problem
# number. DO NOT DELETE OR COMMENT OUT. Replace with relevant info.
print("Brandon Watanabe & Natalie Palos");
print("Project 1 - Python Mine Guesser");
print("");

# Test your board printing functions before continuing
#testBoardPrinting(mineBoard); # TODO 3: Comment out when print methods tested

# Definition of some variables and constants
currScore = 5; # Starting score is 5
minePenalty = 4; # Each time we hit a mine, subtract this value
emptySpaceBonus = 1; # Each time we land on an empty space, add this value
numEmptySpotsFound = 0; # When we reach 20 empty spots, we win!
roundNumber = 1;

# TODO 4: Translate the pseudocode below into Python code
#while current score (currScore) is greater than zero AND the number of empty spots revealed (numEmptySpotsFound) is less than 20
while currScore > 0 and numEmptySpotsFound < 20:
    print ("------------------------------------------")
    # Get row/column guess from user
    row = int(input("Please enter a row number (0-4):"))
    col = int(input("Please enter a col number (0-4):"))
    #print ("Please enter a col number (0-4):")
    #col = int(input())
    # if hidden mine chosen
    if (mineBoard[row][col] == MineCell.HM):
        # Tell user they hit a mine and display points
        print ("You hit a mine! -4 points :-(")
        # Update score
        currScore -= 4
        # Tell user current round/score
        print("After round " + str(roundNumber) + " score is: " + str(currScore))
        # Update board (hidden mine is now revealed mine)
        mineBoard[row][col] = MineCell.RM
    # else if hidden empty chosen
    elif (mineBoard[row][col] == MineCell.HE):
        # Tell user they chose an empty cell and display points
        print("You guessed an empty space! +1 points :-)")
        # Update score
        currScore += 1
        # Tell user current round/score
        print ("After round " + str(roundNumber) + " score is: " + str(currScore))
        # Update board (hidden empty is now revealed empty)
        mineBoard[row][col] = MineCell.RE
    # else
    else:
        # Tell user: "You've already guessed this spot, please try again!"
        print ("You've already guessed this spot, please try again!")
    # call printCurrBoard(mineBoard) to print board
    printCurrBoard(mineBoard)
#printCurrBoard(mineBoard)
    # increment round number
    roundNumber += 1
    #exit the loops by incrementing the numEmptySpotsFound if all of the mine cells are revealed
    numEmptySpotsFound += 1
# Deliver final results...let them know if they won 
# or lost and print the final board
if currScore <= 0:
    print("\n\n*****Oh no, you LOST!!*****\n\nFinal board:")
else:
    print("\n\n*****Nice job, you WIN!!*****\n\nFinal board:")
    
printGameOverBoard(mineBoard)
