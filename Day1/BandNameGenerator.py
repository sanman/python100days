#-----------------------------------------------------------------
# Purpose: Learning print string and input methods
# Created By: Sanjiv Mathur
# Created Date: Dec 5th 2020
# Purpose to modify:
# Modified By:
# Modified Date:
#------------------------------------------------------------------
#1. Craete a greeting for your program,
#2. Ask the user for the city that they grew up in.
#3. Ask the user for the name of a pet.
#4. Combine the name of the city and pet and show their band name.
#5. Make sure that input cursor shows on a new line, see the example at:

print("Welcome to the Band Name generator.")
cityName = input("Which city did you grew up in?\n")
petName = input("What is the name of your pet?\n")
print(f"Your band name could be {cityName.capitalize()} {petName.capitalize()}")