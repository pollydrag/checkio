def checkio(marbles, step):
    pearls = {(marbles.count('w'), marbles.count('b')): 1}

    for s in range(step - 1):
        step_pearls = {}
        for comb, count in pearls.items():
            w, b = comb[0], comb[1]

            if w > 0:
                _comb = (w - 1, b + 1)
                step_pearls[_comb] = step_pearls.get(_comb, 0) + count * w

            if b > 0:
                _comb = (w + 1, b - 1)
                step_pearls[_comb] = step_pearls.get(_comb, 0) + count * b

        pearls = step_pearls

    len_w = sum([w * v for (w, b), v in pearls.items()])
    len_t = sum([(w + b) * v for (w, b), v in pearls.items()])

    return round(len_w / len_t, 2)


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio('bbw', 3) == 0.48, "1st example"
    assert checkio('wwb', 3) == 0.52, "2nd example"
    assert checkio('www', 3) == 0.56, "3rd example"
    assert checkio('bbbb', 1) == 0, "4th example"
    assert checkio('wwbb', 4) == 0.5, "5th example"
    assert checkio('bwbwbwb', 5) == 0.48, "6th example"
