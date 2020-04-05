#PyBank

import os
import csv

csvpath = os.path.join('Resources','budget_data.csv')

months = []
cash = []
changed_cash = []

#Read file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        months.append(row[0])
        cash.append(row[1])

#Length of Months and Sum of cash
total_months = len(months)
Sum = sum(map(int,cash))

#Average change
for i in range(len(cash)-1):
    change = int(cash[i+1]) - int(cash[i])
    changed_cash.append(change)

sum_changed = sum(map(int,changed_cash))
average_changed = round(sum_changed / len(changed_cash),2)

#Max and Min
minimum = min(cash, key=float)
maximum = max(cash, key=float)

#Print all
print()
print("Financial Analysis")
print("------------------")
print("Total Months: " + str(total_months))
print("Total: $" + str(Sum))
print("Average Change: $" + str(average_changed))
print("Greatest Increase in Profits: " + str(months[cash.index(maximum)]) + " ($" + str(maximum) + ")")
print("Greatest Decrease in Profits: " + str(months[cash.index(minimum)]) + " ($" + str(minimum) + ")")
print()

#Output to .txt
output_file = open("PyBank.txt","w")

output_file.write(" \n")
output_file.write("Financial Analysis \n")
output_file.write("------------------ \n")
output_file.write("Total Months: " + str(total_months) + "\n")
output_file.write("Total: $" + str(Sum) + "\n")
output_file.write("Average Change: $" + str(average_changed) + "\n")
output_file.write("Greatest Increase in Profits: " + str(months[cash.index(maximum)]) + " ($" + str(maximum) + ")" + "\n")
output_file.write("Greatest Decrease in Profits: " + str(months[cash.index(minimum)]) + " ($" + str(minimum) + ")" + "\n")

