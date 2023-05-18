from calendar import different_locale
import os
import csv

budget_info = os.path.join("PyBank","Resources","budget_data.csv")

total_months = []
total_profits = []
difference = []

profits = 0
initial_profit = 0
count = 0

with open(budget_info) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)

    for row in csv_reader:
        count = count +1
        total_months.append(row[0])
        total_profits.append(row[1])
        profits=profits + int(row[1])

        final_profit = int(row[1])
        monthly_change = final_profit - initial_profit

        difference.append(monthly_change)

        initial_profit = final_profit 
        
        greatest_increase_profits = max(difference)
        greatest_decrease_profits = min(difference)

        date_increase = total_months[difference.index(greatest_increase_profits)]
        date_decrease = total_months[difference.index(greatest_decrease_profits)]

    print("Financial Analysis")
    print("-----------------------------------")
    print ("Total Months: " + str(count))
    print("Total Profits: " + "$" + str(profits))
    print("Average Change: " + "$" + str(sum(difference)/count))
    print("Greatest Increase in Profits: " + str(date_increase) + " ($" + str(greatest_increase_profits) + ")")
    print("Greatest Decrease in Profits: " + str(date_decrease) + " ($" + str(greatest_decrease_profits) + ")")

    
    output_file = os.path.join("PyBank","Analysis", "pybank_analysis.txt")
