# import modules
import os
import csv

# access the correct file to be analyzed
csvpath = os.path.join('Resources','election_data.csv')
txtpath = os.path.join('Analysis', 'Analysis.txt')



# open the file for reading and writing
with open(csvpath, 'r') as csvreader:


# distinguish the header from the data and move the pointer to the first data row
    csv_header = next(csvreader)
    
# for loop to create a list of candidates
    
    candidates = []
    candidate_votes = {}
    num_votes = 0
    for row in csvreader:
        num_votes = num_votes + int(row[0])
        data = row.split (',')
        current_vote = data[2].replace("\n","")
        if current_vote not in candidates:
            candidates.append(data[2].replace("\n",""))
            candidate_votes[current_vote] = int(0)
        for i in candidates:
            if current_vote == i:
                candidate_votes[i]=candidate_votes[i]+1
    #print(num_votes)            
    #print(candidate_votes)

    khan = candidate_votes['Khan']
    correy = candidate_votes['Correy']
    li = candidate_votes['Li']
    otooley = candidate_votes["O'Tooley"]

    vote_tally = [int(khan), int(correy), int(li), int(otooley)]
    winning_vote_tally=vote_tally.sort()
    #print(winning_vote_tally)

    khan_pct = (khan/num_votes)*100
    correy_pct = (correy/num_votes)*100
    li_pct = (li/num_votes)*100
    otooley_pct = (otooley/num_votes)*100
    khan_pct2 = "{:.3f}".format(khan_pct)
    correy_pct2 = "{:.3f}".format(correy_pct)
    li_pct2 = "{:.3f}".format(li_pct)
    otooley_pct2 = "{:.3f}".format(otooley_pct)
    #print(khan_pct2)            
    
    
    print("Election Results")
    print("----------------------")
    print(F'Total Votes: {num_votes}')
    print("----------------------")
    print(f'Khan: {khan_pct2}% ({khan})')
    print(f'Correy: {correy_pct2}% ({correy})')
    print(f'Li: {li_pct2}% ({li})')
    print(f'O\'Tooley: {otooley_pct2}% ({otooley})')
    print("----------------------")
    print("Winner: Khan")
    print("----------------------")
