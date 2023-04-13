#!/bin/python3
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]
# 1. Calculate the average price of a cut
total_price = 0
for price in prices:
    total_price += price

average_price = total_price / len(prices)

print("Average Haircut Price: " + str(average_price))
# 2. Reduce all prices by 5 dollars
new_prices = [price - 5 for price in prices]
print(new_prices)
# 3. Calculate the total revenue from last week
total_revenue = 0
for i in range(len(hairstyles)):

    total_revenue += prices[i] * last_week[i]

print("Total Revenue: " + str(total_revenue))
# 4. Calculate the average daily revenue
average_daily_revenue = total_revenue / 7
print("Average Daily Revenue: " + str(average_daily_revenue))
# 5. Find all haircuts under 30 dollars
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print(cuts_under_30)
