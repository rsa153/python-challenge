# Modules
import os
import csv

# Set path for file
budget_data = os.path.join("Resources", "budget_data.csv")

# Lists to store data
total_months = 0
revenue = 0
monthly_change = []
month_count = []
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0

# Open and read csv
with open(budget_data, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    row = next(csvreader)

    #Set remaining variables
    previous_profit = int(row[1])
    total_months += 1
    revenue += int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]
    
    # Read each row of data after the header
    for row in csvreader:
        total_months += 1
        revenue += int(row[1])
        
        # Calculate change from current to previous month
        revenue_change = int(row[1]) - previous_profit
        monthly_change.append(revenue_change)
        previous_profit = int(row[1])
        month_count.append(row[0])
        
        # Calculate the greatest increase in profits (date and amount)
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]
        
        # Calculate the greatest decrease in losses (date and amount)
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]  
            
        # Calculate the average of changes in profits/losses and the date
        average_change = sum(monthly_change)/ len(monthly_change)
        high = max(monthly_change)
        low = min(monthly_change)   
            
# Specify file to write to
output_file = os.path.join('analysis', 'pybank.txt')

# Open the txt file and specify the variable that holds the contents of the file
with open(output_file, 'w',) as txtfile:

# Write new data in txtfile
    txtfile.write(f"Financial Analysis\n")