#PyPoll

import os
import csv

csvpath = os.path.join("Resources","election_data.csv")

total_votes = 0

unique_list = []
unique_vote = {}

winner = ""
winner_count = 0

#Read file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        total_votes = total_votes + 1
        
        candidates_names = row[2]
        
        if candidate_names not in unique_list:
            unique_list.append(candidate_names)
            unique_vote[candidate_names] = 0
        unique_vote[candidate_names] = unique_vote[candidate_names] + 1

#Print all
print()
print("Election Results")
print("----------------")
print("Total Votes: " + str(total_votes))
print("----------------")

for candidate in unique_vote:
    votes = unique_vote.get(candidate)
    vote_perc = float(votes) / float(total_votes) * 100
    if (votes > winner_count):
        winner_count = votes
        winner = candidate
    output = f"{candidate}: {vote_perc:.1f}% ({votes})\n"
    print(output, end="")

print("----------------")
print("Winner: " + winner)
print("----------------")
print()

#Output file
output_file = open("PyPoll.txt","w")

output_file.write("\n")
output_file.write("Election Results \n")
output_file.write("---------------- \n")
output_file.write("Total Votes: " + str(total_votes) + "\n")
output_file.write("---------------- \n")
for candidate in unique_vote:
    votes = unique_vote.get(candidate)
    vote_perc = float(votes) / float(total_votes) * 100
    if (votes > winner_count):
        winner_count = votes
        winner = candidate
    output = f"{candidate}: {vote_perc:.1f}% ({votes})\n"
    output_file.write(output)
output_file.write("---------------- \n")
output_file.write("Winner: " + winner + "\n")
output_file.write("---------------- \n")

