#Use Python to calculate the number of seconds in a year
days_in_a_year : int = 365
hours_in_a_day : int = 24
minutes_in_an_hour : int = 60
seconds_in_a_minute : int = 60
total = int(days_in_a_year * hours_in_a_day * minutes_in_an_hour * seconds_in_a_minute )
print(f"The seconds in a year is : {total}")
