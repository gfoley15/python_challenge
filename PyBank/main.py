# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period

# both print the analysis to the terminal and export a text file with the results
# Financial Analysis
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)

### start here, import budget data

import csv

#variables
file_path = "PyBank/Resources/budget_data.csv"
month_count = 0
sum_profit = 0
dates = []



#open budget file
with open(file_path) as budget_data:
    csv_file = csv.reader(budget_data)
    next(csv_file) # skips header row

    for row in csv_file:
        month_count += 1 # add total months, count of each row with data
        # establish index for month, profit/loss amount
        month = row[0]
        profit_loss = int(row[1]) # defining profit_loss as Integer
        sum_profit += profit_loss # adding profit/loss amount to itself for each row



# print the results to the screen
print("Financial Analysis")
print('----------------------------')
print(f'Number of Months: {month_count}')
print(f'Total: ${sum_profit}')
        
# export text file with results