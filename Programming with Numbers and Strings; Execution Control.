################################################
# Program Header
# Course: CIS 117 Python Programming
# Name:   Gerardo Perez
# Description: Python program that will print
#              a discount coupon amount and
#              percentage of purchase for the
#              user through inserting their
#              cost of groceries.
#
# Lab #3 Programming with Numbers and Strings; Execution
#        Control.
# Development Environment: PyCharm 2018.3.3
# Version: Python 3.6.5
# Solution File: gerardoPerezlab3.py
# Date:  02/12/2019
#################################################

# Programs Source Statements

# Define constants for the range of coupon discounts.
MIN_RANGE = 10
LOW_RANGE = 60
MED_RANGE =150
HIGH_RANGE = 210

# Define constants for different coupons
COUPON_ONE = 8
COUPON_TWO = 10
COUPON_THREE = 12
COUPON_FOUR = 14

# Define constant to calculate percentage.
HUNDRED=100

# Obtains the cost of groceries from the users input.
user_Input = float(input("Please enter the cost of your groceries "))

# Computes if cost of groceries is less than the minimum range 10.
if user_Input < MIN_RANGE:
    # If true, prints statement and program quits
    print("You win a discount coupon of $0.00. (0% of your purchase)")
    quit()

# Computes if the cost of groceries is greater than the minimum range 10
# and less than the low range 60.
if MIN_RANGE <= user_Input < LOW_RANGE:
    # If true, computes money spend by applying a percentage to the user input
    # then sets the result into a variable.
    money_spent = user_Input * (COUPON_ONE)/HUNDRED
    # Sets the percent coupon into a float variable.
    percent_coupon = float(COUPON_ONE)

# Computes if the cost of groceries is greater than the low range 60
# and less than the med range 150.
if LOW_RANGE <= user_Input < MED_RANGE:
    # If true, computes money spend by applying a percentage to the user input
    # then sets the result into a variable.
    money_spent = user_Input * (COUPON_TWO)/HUNDRED
    # Sets the percent coupon into a float variable.
    percent_coupon = float(COUPON_TWO)

# Computes if the cost of groceries is greater than the med range 150
# and less than the high range 210.
if MED_RANGE <= user_Input < HIGH_RANGE:
    # If true, computes money spend by applying a percentage to the user input
    # then sets the result into a variable.
    money_spent = user_Input * (COUPON_THREE)/HUNDRED
    # Sets the percent coupon into a float variable.
    percent_coupon = float(COUPON_THREE)

# Computes if the cost of groceries is greater than the high range 210.
if user_Input >= HIGH_RANGE:
    # If true, computes money spend by applying a percentage to the user input
    # then sets the result into a variable.
    money_spent = user_Input * (COUPON_FOUR)/HUNDRED
    # Sets the percent coupon into a float variable.
    percent_coupon = float(COUPON_FOUR)

# Prints a statement of the discount coupon amount and percentage of purchase.
print('You win a discount coupon of ${0:.2f}. ({1:.0f}% of your purchase)'\
      .format(money_spent, percent_coupon))

# Program Output (Commented out)
"""
You win a discount coupon of $0.00. (0% of your purchase)

"""

"""
You win a discount coupon of $2.84. (8% of your purchase)

"""

"""
You win a discount coupon of $7.55. (10% of your purchase)

"""

"""
You win a discount coupon of $19.20. (12% of your purchase)

"""

"""
You win a discount coupon of $31.08. (14% of your purchase)

"""
