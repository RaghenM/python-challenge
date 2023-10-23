#Modules
import os
import csv

# Need to save the file path to access the CSV
election_data = os.path.join("Resources", "election_data.csv")

# set variable to check if we found 
found = False 

# Create the lists to store data. 
count = 0
candidate_list = []
unique_candidate = []
vote_count = []
vote_percent = []

# Open the CSV using the set path PyPollcsv

with open(election_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    # for loop to read through each row of data after header
    for row in csvreader:
        # Count the total number of votes
        count = count + 1
        # Store the candidate names to candidatelist
        candidate_list.append(row[2])
    # Create a set from the candidatelist to get the unique candidate names
    for x in set(candidate_list):
        unique_candidate.append(x)
        # y is the total number of votes per candidate
        y = candidate_list.count(x)
        vote_count.append(y)
        # z is the percent of total votes per candidate
        z = (y/count)*100
        vote_percent.append(z)

    # Winner- using max function (also used in last assignment-ask BCS recommended)    
    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)]
 
print("_____________________________")
print("Election Results")   
print("_____________________________")
print("Total Votes :" + str(count))    
print("_____________________________")
for i in range(len(unique_candidate)):
             # print candidates, formatting for 2 decimal places used code from (https://realpython.com/python-f-strings/)
            print(unique_candidate[i] + ": " + f"{vote_percent[i]}" +"% (" + f"{vote_count[i]}" ")") 
            
print("_____________________________")
print("The winner is: " + winner)
print("_____________________________")

# Print to a text file: election_results.txt
with open('election_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(count) + "\n")
    text.write("---------------------------------------\n")
    # I can't get the 2 decimal place formatting to work without error 
    for i in range(len(set(unique_candidate))):
          text.write(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i]) + ")\n")
    text.write("---------------------------------------\n")
    text.write("The winner is: " + winner + "\n")
    text.write("---------------------------------------\n")