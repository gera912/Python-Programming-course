################################################
# Program Header
# Course: CIS 117 Python Programming
# Name:   Gerardo Perez
# Description: Python program that converts distances in kilometers to
# miles through the use of Object Oriented GUI application. The program
# contains a text entry to enter Kilometers and two buttons "Covert" and
# "Quit". Also, if the entry is not a digit, when convert button
# is clicked, app closes.
#
# Lab #8: GUI Programming Creating a Kilometer to Miles Converter
# Development Environment: PyCharm2018.3
# Version: Python 3.7.3
# Solution File: gerardoPerezLab8.py
# Date:  03/26/2019
#################################################


# Programs Source Statements

from tkinter import *

# Creates a variable for a constant.
KILOMETER_TO_MILE = 0.62137119

class Kilometer_Converter_GUI:
    
    
    def __init__(self):

        # Creates a TK root widget.
        root = Tk()

        # Creates a variable to display the conversion result.
        self.result_variable = StringVar()

        # Creates a Label widget to display kilometer entry.
        self.input_label = Label(root, text = "Enter Kilometers:")

        # Creates a Label widget to display miles.
        self.miles_label = Label(root, text = "Miles =")

        # Creates a Label widget to display result conversion.
        self.result_label = Label(root,textvariable = self.result_variable)

        # Creates an Entry widget for user to enter Kilometers
        self.input_entry = Entry(root)

        # Creates a Button widget for user to click to convert
        # Kilometers to miles.
        self.convert_button = Button(root, text="Convert",\
                                     command = self.convert)

        # Creates a Button widget for user to click to quit app, app closes.
        self.quit_button = Button(root, text = "Quit", command = quit)

        # Creates a Label widget layout orientation through the
        # use of Grid manager.
        self.input_label.grid(row = 0, column = 0)

        # Creates a Entry widget layout orientation through the
        # use of Grid manager.
        self.input_entry.grid(row = 0, column = 1)

        # Creates a Label widget layout orientation through the
        # use of Grid manager.
        self.miles_label.grid(row = 1, column = 0)

        # Creates the Label widget layout orientation through the
        # use of Grid manager.
        self.result_label.grid(row = 1, column = 1)

        # Creates a Button widget layout orientation through the
        # use of Grid manager.
        self.convert_button.grid(row = 2, column = 0)

        # Creates a Button widget layout orientation through the
        # use of Grid manager.
        self.quit_button.grid(row = 2, column = 1)

        # Start the mainloop.
        root.mainloop()


    def convert(self):
        # Checks if entry is a digit, if not a digit program quits.
        # Calculates miles from the kilometers entry through the
        # multiplication of a constant converter.
        try:
            kilometers = float(self.input_entry.get())
        except ValueError:
            quit()
        miles = kilometers*KILOMETER_TO_MILE
        miles = round(miles,2)

        # Sets the miles result to a variable to display in the result
        # Label widget.
        self.result_variable.set(miles)


# Creates an instance of the Kilometer_Converter_GUI class.
gui_run = Kilometer_Converter_GUI()

