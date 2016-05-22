
def longest_palindromic(text):
    longest = str()
    for i in range(len(text)):
        for j in range(len(text), i, -1):
            subsr = text[i:j]
            if len(subsr) > len(longest) and subsr == subsr[::-1]:
                longest = subsr
                break

    return longest

if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"
