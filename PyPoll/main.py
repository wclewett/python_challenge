import os
import csv
import numpy as np

# Define key variables
csvpath = os.path.join("resources", "election_data.csv")    
output_path = os.path.join("analysis", "results.txt")
candidates = []
row_counter = 0
total_votes = 0
votes = {}
winner_votes = 0

# Loop through CSV data to determine how many votes each candidate
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    for row in csvreader:
        row_counter += 1
        if row_counter > 1:
            total_votes += 1
            if row[2] not in candidates:
                candidates.append(row[2])
                votes[f"{row[2]}"] = 0
            for candidate in candidates:
                if candidate == row[2]:
                    votes[f"{row[2]}"] += 1

with open(output_path, 'w') as txtfile:
    txtfile.write("Election Results \n")
    txtfile.write("------------------------- \n")
    txtfile.write(f"Total Votes: {total_votes} \n")
    txtfile.write("------------------------- \n")
    for candidate in candidates:
        if votes[candidate] > winner_votes:
            winner_votes = votes[candidate]
            winner = candidate
        pct_vote = int(np.around(votes[candidate] / total_votes, decimals=3) * 100)
        txtfile.write(f"{candidate}: {pct_vote}.000% ({votes[candidate]}) \n")
    txtfile.write("------------------------- \n")
    txtfile.write(f"Winner: {winner} \n")
    txtfile.write("------------------------- \n")

with open(output_path, "r") as txtfile:
    results = txtfile.read()
    print(results)