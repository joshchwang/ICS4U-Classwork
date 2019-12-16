def bunnyEars(num):
    if num == 0:
        return 0

    return 2 + bunnyEars(num - 1)
