

# -*- coding: UTF-8 -*-

# Import necessary modules to read CSVs
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
    # Track the total number of votes cast
    # Create a dictionary to store candidate name and number of votes
    # Create a string variable for the winning candidate name
    # Create a winning count ticker to add results on top of each other
vote_counter = 0
candidate_votes = {}
winning_candidate = ""
winning_count = 0

# Open the CSV file and process it, skipping the header row
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:
        vote_counter += 1
        candidate_name = row[2]

        #start an if function to parse candidates and votes by name, by checking if they are in the existing dictionary
        #If not, append them to the dictionary, otherwise add a vote to their existing total
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 0
            
        candidate_votes[candidate_name] += 1

    #now that we have gone through the for loop and calculated the total votes, we can use the total to calculate share per candidate
    for candidate, votes in candidate_votes.items():
        vote_percentage = (votes / vote_counter) * 100

        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate
        #create variable that states all candidates and their stats:
        candidate_result = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"

election_results_summary = (
    f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {vote_counter}\n"
    f"-------------------------\n"
    f"Candidate Summary:\n"
)

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"-------------------------\n"
)

print(election_results_summary)
print(candidate_result, end="")
print(winning_candidate_summary)


# Open a text file to save the output
with open(file_to_output, "w") as txt_file:
    txt_file.write(election_results_summary)
    txt_file.write(candidate_result)
    txt_file.write(winning_candidate_summary)
