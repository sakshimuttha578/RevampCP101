# If we list all the natural numebrs below 10 that are multiples of 3 or 5, we get 3,5,6 & 9. The sum of tehre multiples is 23.
# Find the sum of all multiples of 3 and 5 below 1000.

sum = 0
for i in range(1,1000):
    if i %3 == 0 or i%5 == 0:
        sum+=i

print(f"Sum of all multiples of 3 nad 5 below 1000 = {sum}")