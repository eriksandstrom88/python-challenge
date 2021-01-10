# import modules
import os
import csv

# access the correct file to be analyzed
csvpath = os.path.join('Resources','budget_data.csv')
txtpath = os.path.join('Analysis', 'Analysis.txt')

# define a function for the entire analysis
# open the file for reading
with open(csvpath, 'r') as csvreader:

# distinguish the header from the data and move the pointer to the first data row
    csv_header = next(csvreader)

# for loop to create lists of profit/loss and months, then count the length of those lists
    months = []
    profit_loss = []
    for row in csvreader:
        data = row.split(',')
        months.append(data[0])
        profit_loss.append(data[1])
            
# for loop to calculate total profit
    agg_profit = 0
    for pl in profit_loss:
        agg_profit = agg_profit + int(pl)
    # print(f'Total: ${agg_profit}')

# make a list of the change from month to month and take the average
    total_profit = 0
    total_change = 0
    prev_total_profit=0
    monthly_change=[]
    for c in profit_loss:
        prev2_total_profit = prev_total_profit
        prev_total_profit = total_profit
        total_profit = total_profit + int(c)
        current_month_profit = total_profit - prev_total_profit
        prev_month_profit = prev_total_profit - prev2_total_profit
        change = current_month_profit - prev_month_profit
        total_change = total_change + change
        monthly_change.append(change)

    monthly_change.pop(0)
    avg_change = sum(monthly_change)/len(monthly_change)
    avg_change2 = "{:.2f}".format(avg_change)
    
# print(f'Average Change: {avg_change2}')
    sort_monthly_change = []
    for mc in monthly_change:
        sort_monthly_change.append(mc)

    sort_monthly_change.sort()
    grt_decrease_index = monthly_change.index(sort_monthly_change[0])
    grt_increase_index = monthly_change.index(sort_monthly_change[84])
    
    print('Financial Analysis')
    print('-------------------------')
    print(f'Total Months: {len(months)}')
    print(f'Total: ${agg_profit}')
    print(f'Average Change: ${avg_change2}')
    print(f'Greatest Increase in Profits: {months[grt_increase_index+1]} (${sort_monthly_change[84]})')
    print(f'Greatest Decrease in Profits: {months[grt_decrease_index+1]} (${sort_monthly_change[0]})')

    # analysis = open("Analysis","Analysis.txt","w") 
    # analysis.write(
    # print('Financial Analysis')
    # print('-------------------------')
    # print(f'Total Months: {len(months)}')
    # print(f'Total: ${agg_profit}')
    # print(f'Average Change: ${avg_change2}')
    # print(f'Greatest Increase in Profits: {months[grt_increase_index+1]} (${sort_monthly_change[84]})')
    # print(f'Greatest Decrease in Profits: {months[grt_decrease_index+1]} (${sort_monthly_change[0]})'))