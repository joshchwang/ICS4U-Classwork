# Given an integer greater than 9, print its last two
# digits.


a = int(input())
print(str(((a // 10) % 10)) + str(((a % 100) % 10)))
