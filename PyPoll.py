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

# 1. Initialize a total vote counter
total_votes = 0

# 2. Candiate Options
candidate_options = []

# 3. Declare the empty dictionary
candidate_votes = {}

# Open the Election election results and read the file
with open(file_to_load) as election_data:
        # To do: read and analyze the data here
        file_reader = csv.reader(election_data)

        # Read the header row
        headers = next(file_reader) 

        #print(headers) - For printing headers only
        # Print each row in the CSV file
        for row in file_reader:
            
            # 2. Print the candiate name from each row
            candidate_name = row[2]
            # 2. If the candidate does not match any existing candidate
            if candidate_name not in candidate_options:
                # Add it to the list of candidates
                candidate_options.append(candidate_name)
                # 1. Begin tracking that candidate's vote count
                candidate_votes[candidate_name] = 0
            # Add a vote to that candidate's count
            candidate_votes[candidate_name] +=1

        # 1. Add to the total vote count
        total_votes += 1

        # Determine the percentage of votes for each candiate by looping through the counts
        # Iterate through the candidate list
        for candidate_name in candidate_votes:
            # Retreive vote count of a candidate
            votes = candidate_votes[candidate_name]
            # Calculate the percentage of votes
            vote_percentage = float(votes) / float(total_votes) * 100
            # Print the candidate name and percentage of votes
            print(f"{candidate_name}: received {vote_percentage}% of the vote. ")

        # 1. Print the total votes
        print(total_votes)
        # 2. Print the candiate list
        print(candidate_options)
        # 1. Print candidate votes
        print(candidate_votes)

# Close the file
election_data.close()

# Using the with statement open the file as a text file
with open(file_to_save, "w") as txt_file:
    # Write some data to the file
    txt_file.write("Arapahoe, ")
    txt_file.write("Denver, ")
    txt_file.write("Jefferson")
# Close the file


