#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote

#print the analysis to the terminal and export a text file with the results
#Election Results
#Total Votes: 369711
#Charles Casper Stockham: 23.049% (85213)
#Diana DeGette: 73.812% (272892)
#Raymon Anthony Doane: 3.139% (11606)
#Winner: Diana DeGette

### start here, import election data

import csv

# variables
file_path = "PyPoll/Resources/election_data.csv"
vote_count = 0
candidates = []

# open election file
with open(file_path) as election_data:
    csv_file = csv.reader(election_data)
    next(csv_file)
    for row in csv_file:
        vote_count += 1

#print the results
print("Election Results")
print('----------------------------')
print(f'Total Votes: {vote_count}')
print('----------------------------')