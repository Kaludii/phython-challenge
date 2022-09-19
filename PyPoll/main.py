import os
import csv
import sys

# setting the path to the election data csv
electioncsvpath = os.path.join("Resources","election_data.csv")

# path for creating the analysis election results txt file
ElectionResultsPyPolltxt = os.path.join("Analysis","election_results_log.txt")

# making necessary lists
candidatenames = []
votes = 0
Indiv_candidates = []
votes_count = []
vote_percentage = []


with open(electioncsvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        votes = votes + 1
        candidatenames.append(row[2])
    for c in set(candidatenames):
        Indiv_candidates.append(c)
        votes_per_candidate = candidatenames.votes(c)
        votes_count.append(votes_per_candidate)
        votes_per_candidate_percent = (votes_per_candidate/votes)*100
        vote_percentage.append(votes_per_candidate_percent)
        
    winning_vote_count = max(votes_count)
    winner = Indiv_candidates[votes_count.index(winning_vote_count)]
    
# outputs the election results 
print("-------------------------")
print("Election Results")   
print("-------------------------")
print(f"Total Votes : {votes}")    
print("-------------------------")
for i in range(len(Indiv_candidates)):
            print(Indiv_candidates[i] + ": " + str(vote_percentage[i]) +"% (" + str(votes_count[i])+ ")")
print("-------------------------")
print(f"The winner is: {winner}")

# Print to a text file: election_results.txt
# Output perhaps needs to be rounded to 3 decimal points. Leaving that formatting out for now) 

#sys.stdout = open(ElectionResultsPyPolltxt, 'w')
#print("Election Results\n")
#print("---------------------------------------\n")
#print("Total Vote: " + str(votes) + "\n")
#print("---------------------------------------\n")
#for i in range(len(set(Indiv_candidates))):
#            print(Indiv_candidates[i] + ": " + str(vote_percentage[i]) +"% (" + str(votes_count[i]) + ")\n")
#print("---------------------------------------\n")
#print("The winner is: " + winner + "\n")


# whatever is printed will be saved as a txt file in the analysis folder
sys.stdout = open(ElectionResultsPyPolltxt, 'w')
print("-------------------------")
print("Election Results")   
print("-------------------------")
print(f"Total Votes : {votes}")    
print("-------------------------")
for i in range(len(Indiv_candidates)):
            print(Indiv_candidates[i] + ": " + str(vote_percentage[i]) +"% (" + str(votes_count[i])+ ")")
print("-------------------------")
print(f"The winner is: {winner}")