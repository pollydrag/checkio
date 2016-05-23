def checkio(food):
    step = pigeons = 0
    while food > pigeons + step:
        step += 1
        pigeons += step
        food -= pigeons

    return max(pigeons, food)

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(3) == 2, "1st example"
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"
