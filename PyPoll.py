#The data we need to retrieve.
#1. The total number of votes casted
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.

#Add our dependencies.
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv") 
#Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

#1. Initialize total vote counter
total_votes=0

#List of candidates. Declare empty dictionary.
candidate_options=[]
#List of candidates votes. Declare empty dictionary.
candidate_votes={}

# Track winning Candidate, vote count, and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

     # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1

        #Get the candidate name from each row
        candidate_name=row[2]

        # If the candidate does not match any existing candidate add it to the 
        # candidate list
        if candidate_name not in candidate_options:
            # Add candidate name to the list of candidates.
            candidate_options.append(candidate_name)
            
            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

         #Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

#Save the results to our text file
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)   

    for candidate in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print each candidate, their voter count, and percentage to the
        # terminal.
        candidate_results = (f"{candidate}:{vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage
    # Print the winning candidates' results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    #print(winning_candidate_summary)
    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)



