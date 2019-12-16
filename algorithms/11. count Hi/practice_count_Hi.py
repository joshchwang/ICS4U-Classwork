def countHi(string, h=False):
    if len(string) == 0:
        return 0
    
    if string[0] == "h":
        return 0 + countHi(string[1:], True)
    elif string[0] == "i" and h:
        return 1 + countHi(string[1:])
    return 0 + countHi(string[1:])