# python_challenge
The following repo includes two working examples to read a CSV file into Python, extract key data points from the source, and print/export out the data extractions for analysis. Python documentation for dictionary was used as a source of information to assist with data collection and extraction code. Here are the links referenced: 
  - https://docs.python.org/3/library/stdtypes.html#dict.items
  - https://docs.python.org/3/library/stdtypes.html#dict.values
  - https://docs.python.org/3/library/stdtypes.html#range

## PyBank
The task is to create a Python script to analyze the financial records of a company using the provided dataset budget_data.csv. The dataset consists of two columns: "Date" and "Profit/Losses". The script should calculate the following values:

 - Total number of months included in the dataset
 - Net total amount of "Profit/Losses" over the entire period
 - Changes in "Profit/Losses" over the entire period and the average of those changes
 - Greatest increase in profits (date and amount) over the entire period
 - Greatest decrease in profits (date and amount) over the entire period

Scripted process
  - Reading CSV file budget_data into Python
  - Setting variables, lists, dictionaries to collect data for analysis
  - Printing out analysis for collected data to show metrics for months, total profit and change
  - Exporting analysis to new .txt file
    
## PyPoll
The task is to help a small, rural town modernize its vote-counting process using the provided dataset election_data.csv. The dataset consists of three columns: "Voter ID", "County", and "Candidate". The script should calculate the following values:

 - Total number of votes cast
 - Complete list of candidates who received votes
 - Percentage of votes each candidate won
 - Total number of votes each candidate won
 - Winner of the election based on popular vote

Scripted process
  - Reading CSV file election_data into Python
  - Setting variables, lists to collect data for analysis
  - Printing out analysis for collected data to show metrics for candidates and votes
  - Exporting analysis to new .txt file
