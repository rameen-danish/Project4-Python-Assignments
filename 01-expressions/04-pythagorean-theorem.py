#Using the pythagoras theorem calculate the length of hypotenuse BC
import math
sideAB = float(input("Enter the length of side AB: "))
sideAC = float(input("Enter the length of side AC: "))
sideBC = float(math.sqrt(sideAB**2 + sideAC**2))
print(f"The length of Hypotenuse BC is {sideBC}")