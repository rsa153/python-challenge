# Modules
import os
import csv

# Set path for file
budget_data = os.path.join("Resources", "election_data.csv")

# Set variables
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# Open and read csv
with open(budget_data, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row 
    csv_header = next(csvfile)
    
    # Read each row of data after the header
    for row in csvreader:
        
        # Calculate total number of votes
        total_votes += 1
        
        # Calculate total number of votes won by each candidate
        if (row[2] == "Khan"):
            khan_votes += 1
        elif (row[2] == "Correy"):
            correy_votes += 1
        elif (row[2] == "Li"):
            li_votes += 1
        else:
            otooley_votes += 1
            
    # Calculate percent of votes won by each candidate
    kahn_percent = khan_votes / total_votes
    correy_percent = correy_votes / total_votes
    li_percent = li_votes / total_votes
    otooley_percent = otooley_votes / total_votes
    
    # Determine winner of election
    winner = max(khan_votes, correy_votes, li_votes, otooley_votes)

# Display winner of vote
    if winner == khan_votes:
        winner_name = "Khan"
    elif winner == correy_votes:
        winner_name = "Correy"
    elif winner == li_votes:
        winner_name = "Li"
    else:
        winner_name = "O'Tooley" 
        
print(f"Kahn percent: {kahn_percent:.2f}")
print(f"Kahn number of votes: {khan_votes}")
print(f"C percent: {correy_percent:.2f}")
print(f"C number of votes: {correy_votes}")
print(f"L percent: {li_percent:.2f}")
print(f"L number of votes: {li_votes}")
print(f"O percent: {otooley_percent:.2f}")
print(f"O number of votes: {otooley_votes}")
print(f"Total Votes: {total_votes}")
print(f"Winner: {winner_name}")

# Specify file to write to
output_file = os.path.join('analysis', 'election_results.txt')

# Open the txt file and specify the variable that holds the contents of the file
with open(output_file, 'w',) as txtfile:

# Write new data in txtfile
    txtfile.write(f"Election Results\n")