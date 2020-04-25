################################################
# Program Header
# Course: CIS 117 Python Programming
# Name:   Gerardo Perez
# Description: Python program that will take and read filename by the
# user inupt. The program will read all the lines in filename to create a
# dictionary that consist of line numbers for each valid identifier found.
# The program records both line number and identifier and prints them out
# line by line.
#
# Lab #5 Programming with Files; Dictionaries
#        Creating a Dictionary of Identifiers 
# Development Environment: IDLE(Python 3.7 32-bit)
# Version: Python 3.6.5
# Solution File: gerardoPerezlab5.py
# Date:  03/5/2019
#################################################

# Programs Source Statements

# Creates a list of invalid identifiers.
invalid_list=["!","@", "#", "*", "$", "&"]

# Creates an empty dictionary for valid identifiers.
valid_dict={}

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
    
# Creates an empty list for all indentifiers.
identifiers_list=[]

# For loop that will break the space in between lines and make
# a list for indenttifiers.
for line in file_in :

    # Replaces break in between lines for an empty space
    # then sets the result into a variable. 
    list_break = line.replace('\n', ' ')

    # Obtains all identifiers into a list.
    identifiers_list.append(list_break)

# A nested for loop that will first enumarate the identifiers
# in the identifiers list. Then second for loop will
# obtain valid only identifiers into a dictionary. 
for index, result in enumerate(identifiers_list):

    # Computes the identifier in the for loop into a string then
    # sets result into a variable.
    sub_string=str(result)

    # For loop that will go through each character in the string
    # of each identifier.
    for char in sub_string:
        
        # Computes if character in the string of each
        # identifier is in the invalid list.
        if char in invalid_list:

            # if true then break loop.
            break

            # Computes if second character in the string
            # of each identifier is in the invalid list.
            if char in invalid_list:

                # if true then break loop. 
                break

    # computes if all if statements are false then add index plus one, 
    # to start postion at 1, as a key and result as a value to the valid
    # dictionary.  
    else: valid_dict[index+1]=result

# Creates an empty dictionary to flip value to key.
identifier_to_line_number={}

# For loop that will go through keys and values in the valid identifiers
# dictionary.
for line_number, identifier in valid_dict.items():

    # Computes if value is not in the identfier_to_line_number dictionary.
    if identifier not in identifier_to_line_number:

        #if true than the key is added as a value to the
        #identfier_to_line_number dictionary.  
        identifier_to_line_number[identifier] = [line_number]

    else: # if false, than the key is appended to the value of the
          # identfier_to_line_number dictionary.
        identifier_to_line_number[identifier].append(line_number)

# For loop that will go through keys and values in
# identifier_to_line_number dictionary to print identifier
# to line number, line by line.
for identifier, line_number in identifier_to_line_number.items():
    print("%s:%s" % (identifier, line_number))
   
# Program Output (Commented out)
"""
Enter file name to open: t5.py

apple :[1, 11]
1 :[2, 3]
ball :[4, 19]
art :[5]
dog :[6]
pen :[8, 21]
rat :[9]
4 :[10]
carrot :[13]
orange :[15]
ant :[16, 17, 18]
stick :[20]
_ :[22]
goodbye :[25]

"""
