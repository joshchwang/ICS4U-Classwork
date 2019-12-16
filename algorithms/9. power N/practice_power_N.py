def powerN(num, exp):
    if exp == 0:
        return 1
    return num * powerN(num, exp - 1)
