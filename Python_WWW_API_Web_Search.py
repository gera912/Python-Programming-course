# Program Header
# Course: CIS 117 Python Programming
# Name:   Gerardo Perez
# Description: Python program that takes NAS website url as an input,
# downloads the html document and decodes the document into a string.
# A list of topics, that are under review, is created to find the
# number of occurrences of these topics in the NAS website.
#
# Lab #9: Python WWW API Web and Search
#
#
# Development Environment: IDLE(Python 3.7 32-bit)
# Version: Python 3.7.3
# Solution File: gerardoPerezlab9.py
# Date:  04/16/2019
#################################################


# Programs Source Statements

from re import findall
from urllib.request import urlopen
from urllib.error import URLError
import datetime



def main() :

    # Obtains the URL from the users input.
    user_URL = input("Please enter the url, then tab, then enter: ")

    # Creates a list of topics that are under review.
    topics = ['research', 'climate', 'evolution',
              'cultural', 'leadership', 'history']

    # Calls a method to find topics from the URL.
    find_topics(topics, user_URL)


def find_topics(topicsList, URL):
    'prints number of occurrences of topics from URL html document'
    # Finds each topic from list and finds the number of occurrences from
    # the URL html document through the use of re.findall function.
    # Through the use of a dictionary, topics and occurrences are stored and
    # printed.

    # Creates an empty dictionary for the topics and occurrences.
    dictionary = {}

    # Try-except construct to catch an error for opening the url
    try:

        # Creates a variable for decoded and lowercased URL html document.
        html = urlopen(URL).read().decode().lower()

    except (URLError, ValueError) as error:   # checks for specific error

        # Prints statement and program quits.
        print("invalid URL")
        quit()


    # For loop that will go through each topic in the list, add the topic
    # as a key and add the number of occurrence from decoded html URL
    # document as a value.
    for topic in topicsList:

        # Computes if topic is not in the dictionary.
        if topic not in dictionary:

            # If true than the key is added as a topic from the list of
            # topics and through the use of re.findall function, number of
            # occurrences is added as a value.
            dictionary[topic] = len(findall('\\b' + topic + '\\b', html))

    # Prints a statement for the date on the report run.
    print("Today's date is", datetime.date.today())

    # For loop that will go through keys and values in the
    # dictionary to print topic and number of occurrences.
    for topic_key in dictionary:
        print("{0} appears {1} times".\
              format(topic_key,dictionary[topic_key]))

# Call the main function
main()

# Program Output (Commented out)

"""

Today's date is 2019-04-16
research appears 7 times
climate appears 2 times
evolution appears 6 times
cultural appears 8 times
leadership appears 4 times
history appears 4 times


"""
