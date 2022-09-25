# Add our dependencies.
import csv

import os

# Assign a variable for the file to load and path
file_to_load = os.path.join("Resources","election_results.csv")

# Open the election results and read the file
with open(file_to_load) as election_data:
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)
    # Read and print the header row
    headers = next(file_reader)
    print(headers)

# Create  fle name variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis","election_analysis.txt")

# Using the with statement open the file as a text file
with open(file_to_save,"w") as txt_file:

    txt_file.write("Counties in the Election\n")
    txt_file.write("---------------------------\n")
    # Write three counties to the file.
    txt_file.write("Arapahoe\n")
    txt_file.write("Denver\n")
    txt_file.write("Jefferson")


