# -*- coding: utf-8 -*-
"""
Student Do: Trading Log.

This script demonstrates how to perform basic analysis of trading profits/losses
over the course of a month (20 business days).
"""

# @TODO: Initialize the metric variables
total = 0
count = 0
maximum = 0
minimum = 0

# @TODO: Initialize lists to hold profitable and unprofitable day profits/losses
profitable_days = []
unprofitable_days = []

# List of trading profits/losses
trading_pnl = [ -224,  352, 252, 354, -544,
                -650,   56, 123, -43,  254,
                 325, -123,  47, 321,  123,
                 133, -151, 613, 232, -311 ]

# @TODO: Iterate over each element of the list
for daily_pnl in trading_pnl:

    # @TODO: Cumulatively sum up the total and count
    total+= daily_pnl
    count+= 1

    # @TODO: Write logic to determine minimum and maximum values
    if minimum == 0:
        minimum = daily_pnl
    elif daily_pnl < minimum:
        minimum = daily_pnl
    
    if daily_pnl > maximum:
        maximum = daily_pnl

    # @TODO: Write logic to determine profitable vs. unprofitable days
    if daily_pnl > 0:
        profitable_days.append(daily_pnl)
    elif daily_pnl < 0:
        unprofitable_days.append(daily_pnl)

# @TODO: Calculate the average
average = round(total/count, 2)

# @TODO: Calculate count metrics
profitable_count = len(profitable_days)
unprofitable_count = len(unprofitable_days)

# @TODO: Calculate percentage metrics
percentage_profitable = profitable_count/count*100
percentage_unprofitable = unprofitable_count/count*100

# @TODO: Print out the summary statistics
print(f"---------Summary Statistics----------")
print(f"Number of Total Days: {count}")
print(f"Number of Profitable Days: {profitable_count}")
print(f"Number of Unprofitable Days: {unprofitable_count}")
print(f"Percentage of Profitable Days: {percentage_profitable}")
print(f"Percentage of Unprofitable Days: {percentage_unprofitable}")
print(f"-------------------------------------")
print(f"Profitable Days: {profitable_days}")
print(f"Unprofitable Days: {unprofitable_days}")
print(f"-------------------------------------")
print(f"Total Profits/Losses: {total}")
print(f"Daily Average: {average}")
print(f"Worst Loss: {minimum}")
print(f"Best Gain: {maximum}")