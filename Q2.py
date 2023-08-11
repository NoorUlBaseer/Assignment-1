"""Question-2:Leap Year Checker 
Write a program that asks the user to input a year and determines whether the year is a leap year or not. A leap year is either divisible by 4 but not by 100, or divisible by 400.
"""

year = input("Input a year: ")
year = int(year)
if (year % 4 ==0) and (year % 100 != 0) or (year % 400 == 0):
    year = str(year)
    print(year + " is a leap year")
else:
    year = str(year)
    print(year + " is not a leap year")
