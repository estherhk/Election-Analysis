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

#List of candidates. Declare empty list.
candidate_options=[]
#List of candidates votes. Declare empty dictionary.
candidate_votes={}
#CHALLENGE ADDED. List of county. Declare empty list.
county_options=[]
#CHALLENGE ADDED. List of county votes. Delcare empty dictionary.
county_vote={}

# Track winning Candidate, vote count, and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Track largest county
largest_county=""
largest_count=0

#Create a list for counties
counties = ["Arapahoe","Denver","Jefferson"]

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

         #CHALLENGE ADDED. CREATE COUNTY LIST.
        county_name=row[1]

        #CHALLENGE ADDED. If county does not match existing county, add to county list
        if county_name not in county_options:
            #Add county name to list of counties
            county_options.append(county_name)

            #Begin tracking county's count
            county_vote[county_name] = 0

        #CHALLENGE ADDED. Add vote to county's count.
        county_vote[county_name] +=1  
        
#Save the results to our text file
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"\nCounty Votes:\n")


    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    #CHALLENGE ADDED. Find County Results.
    for county in county_vote:
        #Retrieve count and percentage
        count=county_vote[county]
        count_percentage = float(count)/float(total_votes)*100
        #Print each county, count, and percentage
        county_results=(f"{county}:{count_percentage:.1f}% ({count:,})\n")

        #Print each candidate, count, and percentage
        print(county_results)
        #Save county results to text file
        txt_file.write(county_results)

        #Determine Largest County Turnout
        if (count>largest_count):
            largest_count = count
            largest_county = county
    #Print largest county results
    largest_county_turnout = (
        f"\n---------------\n"
        f"Largest County Turnout: {largest_county}\n"
        f"-------------------\n")
    #Save largest country turnout
    txt_file.write(largest_county_turnout)       

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



