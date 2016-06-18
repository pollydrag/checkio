# Solution for "Brackets"
# https://checkio.org/mission/brackets

BRACKETS = {
    ')': '(',
    '}': '{',
    ']': '['
}

def checkio(expression):
    s = []
    for c in expression:
        if c in BRACKETS.values():
            s.append(c)
        if c in BRACKETS.keys():
            if not s or s.pop() != BRACKETS[c]:
                return False
    return not s



#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
