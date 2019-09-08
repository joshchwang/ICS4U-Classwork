# A car can cover distance of N kilometers per day.
# how many days will it take to cover a route of
# length M kilometers? The program gets two numbers:
# N and M.

import math
a = int(input())
b = int(input())
print(math.ceil(b / a))
