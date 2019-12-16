def count8(num, found=False):
    if num == 0:
        return num
    
    if num % 10 == 8 and not found:
        return 1 + count8(num // 10, True)
    elif num % 10 == 8 and found:
        return 2 + count8(num // 10, True)
    return 0 + count8(num // 10)
