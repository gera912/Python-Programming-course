################################################
# Program Header
# Course: CIS 117 Python Programming
# Name:   Gerardo Perez
# Description: Python program that will take a shopping list txt file,
#              of items and their cost. Then create a new list to an output
#              txt file that will left align items, right align prices and
#              display the total of the prices.
#
# Lab #4 Programming with Text Data, Files and Exceptions
#        Your Shopping Budget – The Pricelist
# Development Environment: PyCharm 2018.3.3
# Version: Python 3.6.5
# Solution File: gerardoPerezlab4.py
# Date:  02/19/2019
#################################################

# Programs Source Statements


# Obtains file by user input. Try-except construct to catch
# an invalid input file. If file input is invalid, statement
# is printed and program quits to prevent error message.
try:

    # Obtains the name of file from the users input.
    user_Input=input("Enter file name to open: ")
    file_in=open(user_Input, 'r')         # Opens and read file

except FileNotFoundError:              # checks for specific error

    # Prints statement and program quits.
    print("File not found")
    quit()

# Creates a variable for total of the prices
total=0

# Creates an empty list for items.
items_list=[]

# Creates an empty list of cost of items.
cost_list=[]

# For loop that will break lines into pieces and then into two lists
for line in file_in :

    # Replaces break in between lines for an empty space, splits by
    # colon into 0 and 1 indexes then sets the result into a variable.
    list_break = line.replace('\n', ' ').split(":")

    # Try-except construct to catch an invalid index.
    try:

        # Computes all of index 1 to float and computes
        # the total by adding all of index 1.
        total=float(list_break[1]) + total

        # Obtains all of index 1 items into a list, convert them to float
        # and sets them to two decimal places.
        cost_list.append(format(float(list_break[1]), '.2f'))

    except IndexError:        # checks for specific error,
        pass                  # if error happens then pass error

    # Obtains all of index 0 items into a list
    items_list.append(list_break[0])

# Removes the first item and third from last item from list.
items_list= items_list[1:7] + items_list[8:len(items_list)]

# For loop, that uses the length of cost items, prints two lists
# side by side, left and right aligned to a txt file.
for i in range(len(cost_list)):

    # Prints two lists side by side left and right aligned to a txt file.
    print("{0} {1}".format(items_list[i], str(cost_list[i])\
          .rjust(29-len(items_list[i]))),\
          file=open("gerardoPerezlab4out.txt", "a"))
# Prints a statement for the total of prices, two decimal places,
# into a txt file.
print("Total:{0:>24.2f}".format(total), \
      file=open("gerardoPerezlab4out.txt", "a"))

# Closes file.
file_in.close()

# Program Output (Commented out)
"""
Enter file name to open: lab4.txt

Apples                    0.57
Binder paper              2.29
Cheese                    1.59
Mop                       7.50
Scouring pads             5.00
Shampoo                   2.54
Conditioner               2.79
Ice Cream                 5.89
Total:                   28.17


"""
"""
Enter file name to open: nofile.txt

File not found


"""
