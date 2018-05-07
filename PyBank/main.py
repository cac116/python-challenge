#Import the os module to create file parths accros operating systems
import os

#Import module to read CSVs
import csv

# Specify the file to read from
csvpath = os.path.join('raw_data','budget_data_1.csv')

#We will store our raw data on 'date' and 'revenue' lists
dates_data = []
revenue_data = []
revenue_delta = []

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Loop through csv reader and store raw data on dates_data and revenue_data
    for row in csvreader:
        dates_data.append(row[0])
        revenue_data.append(row[1])   

# Pop out headers 'Date' and 'Revenue' coming from our raw data
dates_data.pop(0)
revenue_data.pop(0)

# Convert all data stored in revenue_data to integers so we can perform operations later on them
for i in range(len(revenue_data)):
    revenue_data[i]=int(revenue_data[i])

#### Total number of months included in the dataset
total_months =len(dates_data)

#### Total amount of revenue gained over the entire period
total_revenue = sum(revenue_data)

# Substracts Next Month's Revenue - Current Month's revenue to
# calculate change in revenue from month to month over the entire period
# This will become a list of month revenue deltas saves in the revenue_delta list
for i in range(len(revenue_data)-1):
    change = revenue_data[i+1]-revenue_data[i]
    revenue_delta.append(change)

# We calculate the Average Revenue Change by dividing the sum of all lists elements by the list length
average_revenue_change = sum(revenue_delta)/len(revenue_delta)

# Greatest revenue change will be the max of the revenue deltas
greatest_increase = max(revenue_delta)
greatest_increase_index = revenue_delta.index(greatest_increase)
greatest_month = dates_data[greatest_increase_index + 1]

# Greatest revenue change will be the min of the revenue deltas
greatest_decrease = min(revenue_delta)
greatest_decrease_index = revenue_delta.index(greatest_decrease)
poorest_month = dates_data[greatest_decrease_index + 1]

# Print results to terminal
print("Financial Analysis")
print("----------------------------")
print("Total Months: ",total_months)
print("Total Revenue: $",total_revenue)
print("Average Revenue Change: $",average_revenue_change)
print("Greatest Increase in Revenue: ",str(greatest_month) + " ($" + str(greatest_increase) + ")")
print("Greatest Decrease in Revenue: ",str(poorest_month) + " ($" + str(greatest_decrease) + ")")

# Specify the file to write to
# Wrioting with this function works like the printing function
output_file = open('main_results.txt','w')
output_file.write("Financial Analysis"+ "\n")
output_file.write("----------------------------"+ "\n")
output_file.write("Total Months: " + str(total_months) + "\n")
output_file.write("Total Revenue: $" + str(total_revenue) + "\n")
output_file.write("Average Revenue Change: $" + str(average_revenue_change) + "\n")
output_file.write("Greatest Increase in Revenue: " + str(greatest_month) + " ($" + str(greatest_increase) + ")"+ "\n")
output_file.write("Greatest Decrease in Revenue: " + str(poorest_month) + " ($" + str(greatest_decrease) + ")")
<<<<<<< HEAD
output_file.close()
=======
output_file.close()
>>>>>>> 2c66e7a7f32873c69f8c7c299d4492b3bca361ec
