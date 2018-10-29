# Solution for "Restricted sum"
# https://checkio.org/mission/restricted-sum/

def checkio(data, i = 0):
    return 0 if i == len(data) else data[i] + checkio(data, i + 1)