import random

rainfall = []

for i in range(11):
    value = random.randint(1, 5)
    rainfall.append(value)

print(rainfall[:7])
print(len(rainfall))

weekly_totals = []

for i in range(0, len(rainfall) - 6, 7):
    week = rainfall[i:i+7]
    total = sum(week)
    weekly_totals.append(total)

print("Weekly totals:", weekly_totals)

maximum = max(rainfall)
minimum = min(rainfall)

print("Maximum rainfall:", maximum)
print("Minimum rainfall:", minimum)

for i, value in enumerate(rainfall):
    if value == maximum:
        print("Maximum rainfall day:", i+1)

    if value == minimum:
        print("Minimum rainfall day:", i+1)

moving_average = []

for i in range(len(rainfall) - 6):
    week = rainfall[i:i+7]
    average = sum(week) / 7
    moving_average.append(round(average, 2))

print("Moving averages:", moving_average)

dry_days = []

for i, value in enumerate(rainfall):
    if value == 0:
        dry_days.append(i+1)

print("Dry days:", dry_days)