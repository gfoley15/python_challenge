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

# variables
file_path = "PyBank/Resources/budget_data.csv"
month_count = 0
sum_profit = 0
dates = [] # list of hold dates for each row
profit_loss_amounts = [] # list to hold profit loss amount for each row
profit_loss_change = {} # dictionary to hold new variable, change

# open budget file
with open(file_path, 'r') as budget_data:
    csv_file = csv.reader(budget_data)
    next(csv_file) # skips header row

    # for loop through each row to count total months and total profit/loss
    # building to 2 lists based on indexed budget data file
    for row in csv_file:
        month_count += 1 # add total months, count of each row with data
        # establish index for month, profit/loss amount
        month = row[0]
        profit_loss = int(row[1]) # defining profit_loss as Integer
        sum_profit += profit_loss # adding profit/loss amount to itself for each row
        dates.append(month) # append date to dates list
        profit_loss_amounts.append(profit_loss) # append amount to profit loss amount list

# defining new variable for added data point called change, using range to allow comparison to previous month
# month[0] does not have a previous month, so starts at month[1]
change = range(1, len(profit_loss_amounts)) 
compared_months = len(profit_loss_amounts) # total rows with comparison data, total compared month number excludes first month 

# for loop through eachitem in range to get calculated change and compared months total for average change metrics
# building dictionary of profit loss changes
for current in change:
    calc_change = profit_loss_amounts[current] - profit_loss_amounts[current - 1] # formula to get change
    profit_loss_change[dates[current]] = calc_change # associating calculated change with appropriate date list index

# defining variables for average change calculation
sum_change = int(sum(profit_loss_change.values()))
compared_months = int(len(profit_loss_change))

# analysis calculations
average_change = round(sum_change / compared_months, 2)
greatest_increase = max(profit_loss_change.values())
greatest_decrease = min(profit_loss_change.values())

# for loop to find max and min date for greatest increase and greatest decrease
# setting max/min dates equal to no value
max_date = "" 
min_date = ""
for date, change in profit_loss_change.items(): # looking over each item in profit/loss change dictionary as date and change
    if change == greatest_increase: # finds greatest increase change value
        max_date = date # sets max date equal to the corresponding date value for that change
    elif change == greatest_decrease: # finds greatest decrease change value
        min_date = date # sets min date equal to the corresponding date value for that change

# print the results to the screen
print("Financial Analysis")
print('----------------------------')
print(f'Number of Months: {month_count}')
print(f'Total: ${sum_profit}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {max_date} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {min_date} (${greatest_decrease})')

# export text file with results
out_file_path = "PyBank/Analysis/financial_analysis.txt"
with open(out_file_path, 'w') as file_out:
    file_out.write("Financial Analysis\n")
    file_out.write('----------------------------\n')
    file_out.write(f'Number of Months: {month_count}\n')
    file_out.write(f'Total: ${sum_profit}\n')
    file_out.write(f'Average Change: ${average_change}\n')
    file_out.write(f'Greatest Increase in Profits: {max_date} (${greatest_increase})\n')
    file_out.write(f'Greatest Decrease in Profits: {min_date} (${greatest_decrease})\n')