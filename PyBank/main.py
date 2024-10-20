# -*- coding: UTF-8 -*-

# Importing Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path ---> need to update
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path ---> need to update

# Define variables to track the financial data
date_counter = 0
total_net = 0

# Add more variables to track other necessary financial data
date = []
Profit_Losses = []
monthly_changes_all = []

highest_rise = {"month": "", "change": 0}
highest_fall = {"month": "", "change": float("inf")}

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)
    header = next(reader)
   
    first_row = next(reader)
    date_counter += 1
    total_net += int(first_row[1])
    previous_value = int(first_row[1])

    # Process each row of data, while creating a dictionary out of the profit/loss statements
    # The length of the list determines the number of months
    for row in reader:
        date.append(row[0])
        Profit_Losses.append(row[1])
        
        #Progressively adding to the value by row, calculate the monthly change, and add changes to a list
        date_counter += 1
        current_value = int(row[1])
        total_net += current_value

        monthly_change = current_value - previous_value
        previous_value = current_value

        monthly_changes_all.append(monthly_change)

        #appending to the highest change/loss dictionaries as we go, replacing current value if higher or lower than the present max/min
        if monthly_change > highest_rise["change"]:
            highest_rise["month"] = row[0]
            highest_rise["change"] = monthly_change

        if monthly_change < highest_fall["change"]:
            highest_fall["month"] = row[0]
            highest_fall["change"] = monthly_change

# Once everything is looped through, we will calculate the average of all changes
def average(monthly_changes_all):
    length = len(Profit_Losses)
    total = 0.0
    for change in monthly_changes_all:
        total += change
    return total/length
average_change = average(monthly_changes_all)

# Generate the output summary

output_summary = (   
    f"Financial Analysis Output\n"
    f"----------------------------\n"
    f"Total Count of Months: {date_counter}\n"
    f"Total Sum of Changes: ${total_net}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Highest Increase in Profits: {highest_rise['month']} (${highest_rise['change']})\n"
    f"Greatest Decrease in Profits: {highest_fall['month']} (${highest_fall['change']})\n"
)

# Print the output
print(output_summary)

# Write the results to a text file
#with open(file_to_output, "w") as txt_file:
   # txt_file.write(output)

with open(file_to_output, "w") as txt_file:
    txt_file.write(output_summary)


