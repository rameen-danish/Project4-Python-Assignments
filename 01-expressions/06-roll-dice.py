#Simulate rolling two dice, and prints results of each roll as well as the total.
import random
die1 = random.randint(1,6)
die2 = random.randint(1,6)
total = int(die1 + die2)
print(f"Die1 = {die1} \nDie2 = {die2} \nTotal of Die1 and Die2 = {total}")