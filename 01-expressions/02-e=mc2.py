#Calculate energy in Joules
from rich import print
C: int = 299792458       #constant valuse of speed of light in m/s
mass_in_kg = float(input("Enter mass in KG: "))
energy_in_joules = float(mass_in_kg * (C**2))

print("Formula of Energy : e = m * C^2")
print(f"Value of Mass: {mass_in_kg}")
print("Value of C = 299792458 ")
print(f"Energy in joules: [bold italic]{energy_in_joules}")
