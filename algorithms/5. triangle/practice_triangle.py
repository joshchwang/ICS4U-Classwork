def triangle(num):
    if num == 0:
        return 0
    
    return num + triangle(num - 1)