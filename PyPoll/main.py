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
    
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvfile)
    row = next(csvreader)

# Specify file to write to
output_file = os.path.join('analysis', 'election_results.txt')

# Open the txt file and specify the variable that holds the contents of the file
with open(output_file, 'w',) as txtfile:

# Write new data in txtfile
    txtfile.write(f"Election Results\n")