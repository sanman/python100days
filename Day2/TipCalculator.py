#-----------------------------------------------------------------
# Purpose: Day 2 final Project to calculate tip
# Created By: Sanjiv Mathur
# Created Date: 6th Dec 2020
#------------------------------------------------------------------
print("Welcome to the tip calculator.")
totalBill = float(input("What was the total bill? $"))
tipPercentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
splitCount = int(input("How many people to split the bill? "))
tipAmount = totalBill*(tipPercentage/100)
tipShare = (totalBill + tipAmount)/splitCount
print(f"Each person should pay: ${round(tipShare, 2)}")