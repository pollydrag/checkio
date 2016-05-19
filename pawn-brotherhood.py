def safe_pawns(pawns):

    def defenders(pawn):
        return chr(ord(pawn[0]) - 1) + str(int(pawn[1]) - 1), chr(ord(pawn[0]) + 1) + str(int(pawn[1]) - 1)

    return len([x for x in pawns if pawns.intersection(set(defenders(x)))])

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
