# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = 'Module 3 - Python\Elections_Analysis\Resources\election_results.csv'

# Assign a variable to save the file to a path.
file_to_save = 'Module 3 - Python\Elections_Analysis\Analysis\election_analysis.txt'

# Open the election results and read the file
with open(file_to_load) as election_data:

# To do: read and analyze the data here.
# Read the file object with the reader function.
     file_reader = csv.reader(election_data)

# Print each row in the CSV file.
     #for row in file_reader:
          #print(row)

     # Read and print JUST the header row.
     headers = next(file_reader)
     print(headers)
