import os
import csv
import sys

# setting the path to the election data csv
electioncsvpath = os.path.join("Resources","election_data.csv")

# path for creating the analysis election results txt file
ElectionResultsPyPolltxt = os.path.join("Analysis","election_results_log.txt")

# making necessary lists
count = 0
candidatelist = []
Indiv_candidates = []
votes_count = []
vote_percentage = []


with open(electioncsvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    # Conduct the ask
    for row in csvreader:
        # Count the total number of votes
        count = count + 1
        # Set the candidate names to candidatelist
        candidatelist.append(row[2])
        # Create a set from the candidatelist to get the unique candidate names
    for x in set(candidatelist):
        Indiv_candidates.append(x)
        # y is the total number of votes per candidate
        y = candidatelist.count(x)
        votes_count.append(y)
        # z is the percent of total votes per candidate
        z = (y/count)*100
        vote_percentage.append(z)
        
    winning_vote_count = max(votes_count)
    winner = Indiv_candidates[votes_count.index(winning_vote_count)]
    
# outputs the election results 
print("-------------------------")
print("Election Results")   
print("-------------------------")
print(f"Total Votes : {count}")    
print("-------------------------")
for i in range(len(Indiv_candidates)):
            print(Indiv_candidates[i] + ": " + str(vote_percentage[i]) +"% (" + str(votes_count[i])+ ")")
print("-------------------------")
print(f"The winner is: {winner}")


# whatever is printed will be saved as a txt file in the analysis folder
sys.stdout = open(ElectionResultsPyPolltxt, 'w')
print("-------------------------")
print("Election Results")   
print("-------------------------")
print(f"Total Votes : {count}")    
print("-------------------------")
for i in range(len(Indiv_candidates)):
           print(Indiv_candidates[i] + ": " + str(vote_percentage[i]) +"% (" + str(votes_count[i])+ ")")
print("-------------------------")
print(f"The winner is: {winner}")