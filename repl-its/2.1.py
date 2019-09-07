# Statement
# Given a two - digit integer, print its left digit
# (a tens digit) and then its right digit
# (a ones digit). Use the operator of integer
# division for obtaining the tens digit and the
# operator of taking remainder for obtaining the
# ones digit.

a = int(input())
print(a // 10, a % 10)
