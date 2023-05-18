# Import dependecies
import os
import csv

# Csv path
pypoll_info = os.path.join("PyPoll","Resources","election_data.csv")

# Define variables
each_vote = 0
voter_index = 1
voter_value = 1
candidates = []
candidate_votes = dict()
list_candidates = [
    "Charles Casper Stockham",
    "Diana DeGette",
    "Raymon Anthony Doane"
]

voting_percent = []


with open(pypoll_info) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)

    for row in csv_reader:
        each_vote = each_vote + 1
        candidates = row[2]
        
        if row[2] not in candidates:
            candidates.append(row[2])
            candidate_votes[row[2]] = 1
        else:
            candidate_votes[row[2]] += 1

for candidate in candidates:
    total_votes = candidate_votes[candidate]
    voting_percent.append(round(float(total_votes) / float(each_vote) * 100,2))

    voter_value.append(round(int(total_votes), 0))

# Finding the winner of election
winner = candidates[voter_index]
    
print("Election Results")   
print("-------------------------")
print(f"Total Votes :" + {each_vote})    
print("-------------------------")
print(f"{list_candidates[0]}: {voting_percent[0]}% ({voter_value[0]})")
print(f"{list_candidates[1]}: {voting_percent[1]}% ({voter_value[1]})")
print(f"{list_candidates[2]}: {voting_percent[2]}% ({voter_value[2]})")
print("------------------------")
print(f"Winner: {winner}")
print("------------------------")


output_file = os.path.join("PyPoll", "Analysis", "election_analysis.txt")

        
