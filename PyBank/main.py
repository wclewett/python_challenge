import os
import csv
import numpy as np

# Define key variables
csvpath = os.path.join("resources", "budget_data.csv")  # filepath for csv formatted input data
output_path = os.path.join("analysis", "results.txt")   # filepath for txt formatted results
month_count = 0                                         # counter for months analyzed
profit_loss_list = []                                   # summary list for each month's profit or loss
delta_list = []                                         # summary list for the change between each month's profit/loss

# Loop through CSV data for monthly values
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    for row in csvreader:
        month_count += 1
        if month_count >=2:
            profit_loss_list.append(int(row[1]))
            if month_count == 3:
                delta = profit_loss_list[month_count - 2] - profit_loss_list[month_count - 3]
                delta_list.append(delta)
            if month_count >= 4:
                delta = profit_loss_list[month_count - 2] - profit_loss_list[month_count - 3]
                if delta > np.max(delta_list):
                    max_inc_date = row[0]
                if delta < np.min(delta_list):
                    max_dec_date = row[0]
                delta_list.append(delta)
                

total_months_analyzed = month_count
total_profit_loss = sum(profit_loss_list)
average_change = np.around(np.mean(delta_list), decimals=2)
max_inc = np.max(delta_list)
max_dec = np.min(delta_list)

with open (output_path, 'w') as txtfile:
    txtfile.write("Fianacial Analysis \n")
    txtfile.write("-------------------------------------------------------- \n")
    txtfile.write(f"Total P/L: {total_profit_loss} \n")
    txtfile.write(f"Average Change (Monthly): $ ({average_change}) \n")
    txtfile.write(f"Max Increase in P/L (Monthly): {max_inc_date} $ {max_inc} \n")
    txtfile.write(f"Max Increase in P/L (Monthly): {max_dec_date} $ ({max_dec}) \n")
    txtfile.write("-------------------------------------------------------- \n")

with open(output_path, "r") as txtfile:
    results = txtfile.read()
    print(results)