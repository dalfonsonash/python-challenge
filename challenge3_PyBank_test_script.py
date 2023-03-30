import csv

# Open the CSV file and read its contents
with open('budget_data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row

    # Initialize variables
    months_count = 0
    net_total = 0
    prev_profit = 0
    profit_changes = []
    max_increase = 0
    max_decrease = 0

    # Loop through the rows of the CSV file
    for row in reader:
        # Extract the date and profit/loss from the row
        date = row[0]
        profit = int(row[1])

        # Update the total number of months and net total
        months_count += 1
        net_total += profit

        # Calculate the change in profit since the previous month
        if months_count > 1:
            change = profit - prev_profit
            profit_changes.append(change)

            # Update the max increase and max decrease
            if change > max_increase:
                max_increase = change
                max_increase_date = date
            elif change < max_decrease:
                max_decrease = change
                max_decrease_date = date

        # Store the current profit for the next iteration
        prev_profit = profit

    # Calculate the average change in profit
    avg_change = sum(profit_changes) / len(profit_changes)

    # Print the analysis results
    print("Financial Analysis")
    print("------------------")
    print(f"Total Months: {months_count}")
    print(f"Total: ${net_total}")
    print(f"Average Change: ${avg_change:.2f}")
    print(f"Greatest Increase in Profits: {max_increase_date} (${max_increase})")
    print(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})")

 # Export the analysis results to a text file
    with open("..\python-challenge\PyBank\analysis\budget_analysis.txt", "w") as output_file:
        output_file.write("Financial Analysis\n")
        output_file.write("------------------\n")
        output_file.write(f"Total Months: {months_count}\n")
        output_file.write(f"Total: ${net_total}\n")
        output_file.write(f"Average Change: ${avg_change:.2f}\n")
        output_file.write(f"Greatest Increase in Profits: {max_increase_date} (${max_increase})\n")
        output_file.write(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})\n")

    print("The analysis has been exported to budget_analysis.txt.")