from rich import print
degrees_fahrenheit : str = input("Enter temperature in Fahrenhite! ")
degrees_fahrenheit : float = float(degrees_fahrenheit)
degrees_celsius : float = (degrees_fahrenheit - 32) * 5.0/9.0
print(f"Temperatue : [bold italic]{degrees_fahrenheit}F = {degrees_celsius}C") 