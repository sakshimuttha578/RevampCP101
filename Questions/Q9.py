# Q9. Convert Days to Weeks and Days
# d = 45. Convert 45 days → 6 weeks and 3 days.

d = 45
weeks = round(d/7)
days = d % 7

print(f"{d} days = {weeks} weeks & {days} days")