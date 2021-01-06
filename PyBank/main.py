# Modules
import os
import csv

# Set path for file
budget_data = os.path.join("Resources", "budget_data.csv")

# Open and read csv
with open(budget_data, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    row = next(csvreader)

# Specify file to write to
output_file = os.path.join('analysis', 'pybank.txt')

# Open the txt file and specify the variable that holds the contents of the file
with open(output_file, 'w',) as txtfile:

# Write new data in txtfile
    txtfile.write(f"Financial Analysis\n")