# Days of the week are numbered as: 0 - Sunday,
# 1 - Monday, 2 - Tuesday, ... 6 - Saturday. An
# integer K in the range 1 to 365 is given. Find the
# number of day of week for K - th day of year
# provided that in this year January 1 was Thursday.

k = int(input())
print((k + 3) % 7)
