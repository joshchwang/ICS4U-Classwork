def bunnyEars2(num):
    if num == 0:
        return 0
    
    if num % 2 == 0:
        return 3 + bunnyEars2(num - 1)
    return 2 + bunnyEars2(num - 1)
