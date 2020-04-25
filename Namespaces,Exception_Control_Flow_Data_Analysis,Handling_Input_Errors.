################################################
# Program Header
# Course: CIS 117 Python Programming
# Name:   Gerardo Perez
# Description: Python program that will take and read filename by the
# user inupt. The program will read all the lines in filename and enforce
# expectations of a data set: file must exist, file must start with an
# integer and the file must contain n data values, n data values is the
# first line. The program lets user run 5 readable file runs
#
# Lab #6 Programming with Namespaces, Exception Control
#        Flow Data Analysis and Handling Input Errors.
#       
# Development Environment: IDLE(Python 3.7 32-bit)
# Version: Python 3.6.5
# Solution File: gerardoPerezlab6.py
# Date:  03/12/2019
#################################################




def main():

    # Creates a variable for a stop flag to end the while loop.
    done = False
    
    # Creates a variable for a count of read file runs.
    count = 0

    # While loop to continue reading files.
    while not done:

        # Try-except construct to catch an file not found error.
        try:
            # Obtains the name of file from the users input.
            user_Input = input("Enter file name to open: ")
            file_in = open(user_Input, 'r')         # Opens and read file
           
        except FileNotFoundError:           # checks for specific error

            # Prints statement and program continues.
            print("Error: File not found")
            continue
            
        # Creates an empty list for values.    
        list = []

        # Creates an empty list for integer values.
        int_list = []

        # For loop that will break the space in between lines and make
        # a list for values.
        for line in file_in:

            # Replaces break in between lines for an empty space
            # then sets the result into a variable. 
            list_break = line.replace('\n', ' ')

            # Obtains all values into a list.
            list.append(list_break)

        # Try-except construct to catch an file not found error.
        try:

           # For loop that will go through values in list and
           # covert to integers and append to the the integer list.
            for value in list:
                int_list.append(int(value))
               
        except ValueError:            # checks for specific error
            
           # Prints statement 
            print("Error: file contents invalid")

            # Increases the count to 1 for a readable run
            count = count + 1

            # If statement that checks if readable run count is 5.
            if count == 5:

                # if true then the stop flag variable is set to True.
                #Stops while loop.
                done = True
            continue

        
        
        # Removes the first item of the integer list.
        int_list = int_list[1:len(list)]

        # Creates a variable for the number of data values given from file
        n_value = int((list[0]))

        # Creates a variable for the actual number of data value.
        total_values = int(len(int_list))

        # If statement that checks if the the given and actual number of
        # data values do not match.
        if total_values != n_value:

            #if true than statement is printed.
            print("Error: The file must contain n data values.")

            # Increases the count to 1 for a readable run
            count = count + 1

            # If statement that checks if readable run count is 5.
            if count == 5:

                # if true then the stop flag variable is set to True.
                #Stops while loop.
                done = True
            continue

        else: # if false, than stament is printed with sum.
            print("The sum is:",(sum(int_list)))

            # Increases the count to 1 for a readable run
            count = count + 1

            # If statement that checks if readable run count is 5.
            if count == 5:

                # if true then the stop flag variable is set to True.
                #Stops while loop.
                done = True
            continue
      
         
main()



# Program Output (Commented out)
"""

Enter file name to open: bad1.dat
Error: The file must contain n data values.

Enter file name to open: bad2.dat
Error: file contents invalid

Enter file name to open: bad3.dat
Error: file contents invalid

Enter file name to open: bad4.dat
Error: The file must contain n data values.

Enter file name to open: good.dat
The sum is: 55



"""

