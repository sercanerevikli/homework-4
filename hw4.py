year = int(input("What is your birth year: "))

if 1928<= year <=1945:
    print("You are a Silent Generation.")
elif 1946<= year <=1964:
    print("You are a Baby Boomers.")
elif 1965<= year <=1980:
    print("You are a Generation-X.")
elif 1981<= year <=1996:
    print("You are a Generation-Y.")
elif 1997<= year <=2012:
    print("You are a Generation-Z.")
elif 2013<= year <=2020:
    print("You are a Generation Alpha.")

import sys
sys.exit(0)