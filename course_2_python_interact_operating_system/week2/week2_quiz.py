#!/usr/bin/env python3.7

import os
import csv

##################################################################
##																##
##  			Question #1										##
##	Process create_file() as a DictReader and process file out	##
##################################################################


# Create a file with data in it

def create_file(filename):
    with open(filename, "w") as file:
        file.write("name,color,type\n")
        file.write("carnation,pink,annual\n")
        file.write("daffodil,yellow,perennial\n")
        file.write("iris,blue,perennial\n")
        file.write("poinsettia,red,perennial\n")
        file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row


def contents_of_file(filename):
    return_string = ""

    # Call the function to create the file
    create_file(filename)

    # Open the file
    with open(filename) as read_dict:
        # Read the rows of the file into a dictionary
        reader = csv.DictReader(read_dict)
        # Process each item of the dictionary
        for row in reader:
            return_string += "a {} {} is {}\n".format(
                row["color"], row["name"], row["type"])
    return return_string


# Call the function
print(contents_of_file("flowers.csv"))


##################################################################
##																##
##  			Question #2										##
##	Processes same as above with out turning it into a dict		##
##################################################################

# Create a file with data in it
def create_file(filename):
    with open(filename, "w") as file:
        file.write("name,color,type\n")
        file.write("carnation,pink,annual\n")
        file.write("daffodil,yellow,perennial\n")
        file.write("iris,blue,perennial\n")
        file.write("poinsettia,red,perennial\n")
        file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row


def contents_of_file(filename):
    return_string = ""

    # Call the function to create the file
    create_file(filename)

    # Open the file
    with open(filename) as reader:
        # Read the rows of the file
        rows = csv.reader(reader)
        next(rows)
        # Process each row
        for row in rows:
            name, color, type = row
            # Format the return string for data rows only

            return_string += "a {} {} is {}\n".format(color, name, type)
    return return_string


# Call the function
print(contents_of_file("flowers.csv"))
