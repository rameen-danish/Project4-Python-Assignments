from rich import print
print("Perimeter of Triangle")
side1 : float = float(input("Enter the length of side 1: "))
side2 : float = float(input("Enter the length of side 2: "))
side3 : float = float(input("Enter the length of side 3: "))
perimeter : float = side1+side2+side3
print(f"The Perimeter of Triangle is [bold italic]{perimeter}")