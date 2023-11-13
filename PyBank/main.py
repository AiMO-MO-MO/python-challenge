
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

    for row in csvreader:
        date = row[0]
        pl = int(row[1])
        total_months = total_months + 1
        total_pl = total_pl + pl
        



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
print(average_change)         

#defining the script to run on the inputed data
def profit_loss(budget_data):
    
    #creating variables for the data
    date = int(budget_data[0])
    pl = int(budget_csv[1])

    #count the total number of months
    total_months = 0
    for count in date:
        total_months = count + 1

    #total of the profit/loss column     
    total_pl = 0     
    for c in pl:
        total_pl = int(c + total_pl)  


    #average of profit/loss
    total = 0
    for numbers in pl:
        length = len(pl)
        total += numbers
    return total / length 

    #greatest increas
    idecrease = min(pl)
    g_increase = decrease
    
  
    #greatest decrease
    decrease = min(pl)
    g_decrease = decrease





# writing new csv
output_path = os.path.join("analysis", "PyBank_output.txt")

with open(output_path, 'w') as txtfile:
    

    txtfile.write("test")
