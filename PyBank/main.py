import csv
import os
import sys

# path for the csv file
budgetcsvpath = os.path.join("Resources","budget_data.csv")

# path for creating the analysis txt file
AnalysisPyBanktxt = os.path.join("Analysis","analysis_log.txt")

# making necessary lists for the profits, monthly changes and dates.
profits = []
dates = []
changesmonthly = []

# making basic variables
#start from here 
total_months = 0
total_profit = 0
change_in_profits = 0
starting_profit = 0


with open(budgetcsvpath, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csv_reader)

    for row in csv_reader:    
      total_months = total_months + 1 

      dates.append(row[0])

      profits.append(row[1])
      total_profit = total_profit + int(row[1])

      final_profit = int(row[1])
      monthly_profits_change = final_profit - starting_profit

      changesmonthly.append(monthly_profits_change)

      change_in_profits = change_in_profits + monthly_profits_change
      starting_profit = final_profit

      # will find avg change in the profits
      average_change_profits = (change_in_profits/total_months)
      
      greatest_increase_profits = max(changesmonthly)
      greatest_decrease_profits = min(changesmonthly)

      increase_in_dates = dates[changesmonthly.index(greatest_increase_profits)]
      decrease_in_dates = dates[changesmonthly.index(greatest_decrease_profits)]
  
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total Profits: ${total_profit}")
    print(f"Average Change: ${average_change_profits}")
    print("Greatest Increase in Profits: " + str(increase_in_dates) + " ($" + str(greatest_increase_profits) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_in_dates) + " ($" + str(greatest_decrease_profits)+ ")")

# delete this sectioN?
with open('financial_analysis.txt', 'w') as text:
    text.write("  Financial Analysis"+ "\n")
    print("----------------------------")
    text.write("    Total Months: " + str(total_months) + "\n")
    text.write("    Total Profits: " + "$" + str(total_profit) +"\n")
    text.write("    Average Change: " + '$' + str(int(average_change_profits)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(increase_in_dates) + " ($" + str(greatest_increase_profits) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(decrease_in_dates) + " ($" + str(greatest_decrease_profits) + ")\n")

# whatever is printed will be saved as a txt file in the analysis folder
sys.stdout = open(AnalysisPyBanktxt, 'w')
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total Profits: ${total_profit}")
print(f"Average Change: ${average_change_profits}")
print("Greatest Increase in Profits: " + str(increase_in_dates) + " ($" + str(greatest_increase_profits) + ")")
print("Greatest Decrease in Profits: " + str(decrease_in_dates) + " ($" + str(greatest_decrease_profits)+ ")")
