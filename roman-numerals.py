roman = [
    ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
    ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
    ['C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
    ['M', 'MM', 'MMM'],
]


def checkio(data):
    return ''.join([roman[i][int(l) - 1] for i, l in enumerate(str(data)[::-1]) if int(l)][::-1])


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    assert checkio(10) == 'X', '10'
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
