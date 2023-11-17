
#importing libraries
import os
import csv

#creating the join to the dataset within the Resources folder
budget_csv = os.path.join('Resources', 'budget_data.csv')

total_months = 0
total_pl    = 0
net_change_list =[]
max_increase_net = 0
max_increase_date = ""
max_decrease_net = 0
max_decrease_date = ""

# opening the CSV file 
with open(budget_csv, 'r') as csvfile:
    csvreader =csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    #for loop to run through the CSV data rows
    for row in csvreader:

        #create variables for data
        date = row[0]
        pl = int(row[1])

        #count of total months and Profit/Loss
        total_months = total_months + 1
        total_pl = total_pl + pl
        


        # average/min/max difference between months
        if total_months > 1:
            net_change = pl - previous_pl
            net_change_list.append(net_change)

            if net_change > max_increase_net:
                max_increase_net = net_change
                max_increase_date = date

            if net_change < max_decrease_net:
                max_decrease_net = net_change
                max_decrease_date = date


        previous_pl = pl


average_change = sum(net_change_list) / len(net_change_list)
       

# writing new csv
output_path = os.path.join("analysis", "PyBank_output.txt")

with open(output_path, 'w') as txtfile:

    #create output file
    
    output_file = '''Financial Analysis\n --------------------------\n
    Total Months:   ''' + str(total_months) +'''\n
    Total:   $ '''+ str(total_pl) + '''\n
    Average:   $ '''+ str(average_change) + '''\n
    Greatest Increase:    '''+ max_increase_date  +   ''' $( '''+ str(max_increase_net) + ''')\n
    Greatest Decrease:    ''' + max_decrease_date +    '''$( '''+ str(max_decrease_net) + ''')\n'''
                
    print(output_file)

    txtfile.write(output_file)
