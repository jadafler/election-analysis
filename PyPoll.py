# The data we need to retreive
# 1. The total number of votes cast
# 2. A complete list of candiates who received votes
# 3. The percentage of votes each candiate won
# 4. The total number of votes each candiate won
# 5. The winner of the election based on popular vote

import csv
import os 
# Assign a variable to load a file from a path
file_to_load = 'Resources/election_results.csv'
# Assign a variable to save the file to a path
file_to_save = os.path.join("Resources", "election_analysis.txt")
# Open the Election election results and read the file
with open(file_to_load) as election_data:
        # To do: read and analyze the data here
        file_reader = csv.reader(election_data)
        # Print each row in the CSV file
        #headers = next(file_reader)
        #print(headers)
        for row in file_reader:
            print(row)
# Close the file
election_data.close()

# Using the with statement open the file as a text file
with open(file_to_save, "w") as txt_file:
    # Write some data to the file
    txt_file.write("Arapahoe, ")
    txt_file.write("Denver, ")
    txt_file.write("Jefferson")
# Close the file


