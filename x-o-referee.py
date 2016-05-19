def checkio(game_result):

    def check_row(row, func=all):
        for l in 'XO':
            if func([r == l for r in row]):
                return l
        return 'D'

    m = [check_row(r) for r in game_result]  # rows
    m += [check_row(r) for r in zip(*game_result)]  # columns
    m += check_row(list(map(str.__getitem__, game_result, [0, 1, 2])))  # main diagonal
    m += check_row(list(map(str.__getitem__, game_result, [2, 1, 0])))  # secondary diagonal

    return check_row(m, any)

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"

