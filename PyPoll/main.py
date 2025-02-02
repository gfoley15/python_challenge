### start here, import election data

import csv

# variables
file_path = "PyPoll/Resources/election_data.csv"
vote_count = 0
candidates = []
candidate_votes = []

# open election file
with open(file_path, 'r') as election_data:
    csv_file = csv.reader(election_data)
    next(csv_file) # skips a row in the file, the header row
    # read a row in the file
    for row in csv_file:
        vote_count += 1 # add to total votes
        # establish index for ballot id, county, candidate
        ballot_id = row[0]
        county = row[1]
        candidate = row[2]
        # check to see if the candidate exists
        if candidate not in candidates:
            candidates.append(candidate) # add candidate to the list if they are not in the list
            candidate_votes.append(1) # add the first vote
        else: # candidate is in the list
            candidate_id = candidates.index(candidate) # establish index for candidate
            candidate_votes[candidate_id] += 1 # add the next votes
# done reading the file

# find the winner
winner = candidates[candidate_votes.index(max(candidate_votes))]

# print the results to the screen
print("Election Results")
print('----------------------------')
print(f'Total Votes: {vote_count}')
print('----------------------------')
for candidate in candidates:
    current_candidate_votes = candidate_votes[candidates.index(candidate)] # varible inside for loop for unique candidate vote count
    vote_percentage = round((current_candidate_votes / vote_count)*100, 3) # variable inside for loop for calculating percent of vote for each candiate
    print(f'{candidate}: {vote_percentage}% ({current_candidate_votes})')
print('----------------------------')
print(f'Winner: {winner}')
print('----------------------------')

# export text file with results
out_file_path = "PyPoll\Analysis\election_results.txt"
with open(out_file_path, 'w') as file_out:
    file_out.write("Election Results\n")
    file_out.write('----------------------------\n')
    file_out.write(f'Total Votes: {vote_count}\n')
    file_out.write('----------------------------\n')
    for candidate in candidates:
        current_candidate_votes = candidate_votes[candidates.index(candidate)] # varible inside for loop for unique candidate vote count
        vote_percentage = round((current_candidate_votes / vote_count)*100, 3) # variable inside for loop for calculating percent of vote for each candiate
        file_out.write(f'{candidate}: {vote_percentage}% ({current_candidate_votes})\n')
    file_out.write('----------------------------\n')
    file_out.write(f'Winner: {winner}\n')
    file_out.write('----------------------------\n')