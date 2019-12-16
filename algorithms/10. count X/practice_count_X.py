def countX(string):
    if len(string) == 0:
        return 0
    
    if string[0] == "x":
        return 1 + countX(string[1:])
    else:
        return 0 + countX(string[1:])

print(countX("xxhixx"))