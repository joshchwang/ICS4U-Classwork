def sumDigits(num):
    if num < 10:
        return num

    return num % 10 + sumDigits(num // 10)
