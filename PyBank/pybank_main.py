#Modules
import os
import csv

# Need to save the file path to access the CSV
budget_data = os.path.join("Resources", "budget_data.csv")

# set variable to check if we found 
found = False 

# open and read csv (If csvfile is a file object, it should be opened with newline='')
with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
  

    # Create the list used to store and find net amount of profit and loss
    profit_loss = []
    months = []

    #for loop to read through each row of data after header
    for rows in csvreader:
        profit_loss.append(int(rows[1]))
        months.append(rows[0])

    # Creat the list used to store and find revenue change
    revenue_change = []

    for x in range(1, len(profit_loss)):
        revenue_change.append((int(profit_loss[x]) - int(profit_loss[x-1])))
    
    # calculate average revenue change
    revenue_average = sum(revenue_change) / len(revenue_change)
    
    # calculate total length of months
    total_months = len(months)

    # greatest increase in revenue using max function (also used in last assignment-ask BCS recommended)
    greatest_increase = max(revenue_change)

    # greatest decrease in revenue using min function (also used in last assignment- ask BCS recommended)
    greatest_decrease = min(revenue_change)


    # print the Results in GitBash
    print("Financial Analysis")

    print("____________________________________________")

    # pring Total Months as a string 
    print("Total Months: " + str(total_months))

    # print Total as a string
    print("Total: " + "$" + str(sum(profit_loss)))

    # print"Average Change, formatting for 2 decimal places used code from (https://realpython.com/python-f-strings/)
    print (f"Average Change: ${revenue_average:.2f}")

    print("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "($" + f"{greatest_increase}" ")")

    print("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "($" + f"{greatest_decrease}" ")")


   