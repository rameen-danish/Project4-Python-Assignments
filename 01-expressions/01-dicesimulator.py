"""
Program: dicesimulator
----------------------
Simulate rolling two dice, three times.  Prints
the results of each die roll.  This program is used
to show how variable scope works.
"""

# Import the random library which lets us simulate random things like dice!
import random

NUM_SIDES = 6

def roll_dice():
    die1: int = random.randint(1, NUM_SIDES)
    die2: int = random.randint(1, NUM_SIDES)
    print(f"Die 1 = {die1}, Die 2 = {die2}")

def main():
    roll_dice()
    roll_dice()
    roll_dice()

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()