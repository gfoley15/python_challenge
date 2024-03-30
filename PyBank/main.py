#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The changes in "Profit/Losses" over the entire period, and then the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period

#both print the analysis to the terminal and export a text file with the results
#Financial Analysis
#Total Months: 86
#Total: $22564198
#Average Change: $-8311.11
#Greatest Increase in Profits: Aug-16 ($1862002)
#Greatest Decrease in Profits: Feb-14 ($-1825558)

# import election data

import csv
file_path = "PyPoll/Resources/budget_data.csv"

with open(file_path, 'r') as text:
    csv_file = csv.reader(text)

    for row in csv_file:
       