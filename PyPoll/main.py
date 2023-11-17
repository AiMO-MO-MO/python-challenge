#importing libraries
import os
import csv

#creating the join to the dataset within the Resources folder
election_csv = os.path.join('Resource', 'election_data.csv')

total_votes = 0
pol_votes = 0
votes_list = []
county_list = []
candidate_list = []
voter_dict = {}

#opening the CSV file 
with open(election_csv, 'r') as csvfile:
    csvreader =csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    #for loop to run through the CSV data rows
    for row in csvreader:


        b_id = int(row[0])
        county = row[1]
        candidate = row[2]

        #counting for total votes and adding to the lists

        total_votes = total_votes + 1
        candidate_list.append(candidate)
        county_list.append(county)
        #determining if the candidate exists in dictionary and adding
        if candidate not in voter_dict:
            voter_dict[candidate] = 1
            
        else:
            voter_dict[candidate] = voter_dict[candidate] + 1   
                
    #finding the winner by higherst number in the dictionary value
    winner_count = 0
    winner_key = ""
    for i in voter_dict:
        if voter_dict[i] > winner_count:
            winner_count = voter_dict[i]
            winner_key = i
    winner = winner_key

    
#creating output path
output_path = os.path.join("analysis", "PyPoll_output.txt")

with open(output_path, 'w') as txtfile:

#creating output file
    output_file = print("Election Results\n",
                "--------------------------\n",
                "Total Votes:   " + str(total_votes) + "\n",
                "--------------------------\n")

    for candidate, value in voter_dict.items():
        percentage = (value/total_votes) * 100
        f_percentage = "{:.3f}%".format(percentage)
        voter_roll = f"Candidate: {candidate}: {f_percentage} ({value})"

        print(f'{voter_roll}')

    print("--------------------------\n",
        "Winner:   " + str(winner) + "\n",
        "--------------------------\n" )

#printing result
    print(output_file)
#write file
    txtfile.write(output_file)
