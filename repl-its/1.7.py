# Statement
# Given two timestamps of the same day: a number of
# hours, minutes and seconds for both of the
# timestamps. The moment of the first timestamp
# happened before the moment of the second one.
# Calculate how many seconds passed between them.

a = int(input())
b = int(input())
c = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())

print((a2 * 3600 + b2 * 60 + c2) -
      (a * 3600 + b * 60 + c))
