def count7(num):
    if num == 0:
        return num
    
    if num % 10 == 7:
        return 1 + count7(num // 10)
    return 0 + count7(num // 10)
