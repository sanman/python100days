#-----------------------------------------------------------------
# Purpose: Practice Exercise day 2
# Created By: Sanjiv Mathur
# Created Date: Dec 6th 2020
#------------------------------------------------------------------
# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# The BMI is a measure of some's weight taking into account their height. e.g. If a tall person and
# a short person both weigh the same amount, the short person is usually more overweight.
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
#--------Hints----------------------
# Check the data type of the inputs.
# Try to use the exponent operator in your code.
# Remember PEMDAS.
# Remember to convert your result to a whole number (int).


def is_float(value):
    if "." in value:
        value = float(value)
    else:
        value = int(value)
    return value
# Don't change the code below
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# Don't change the code above 👆

BMI = is_float(weight)/(is_float(height)**2)
print(BMI)


