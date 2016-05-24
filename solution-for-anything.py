def checkio(anything):
    f = (lambda x, y: True)
    return type('', (), {
        '__lt__': f,
        '__le__': f,
        '__eq__': f,
        '__ne__': f,
        '__gt__': f,
        '__ge__': f
    })()

if __name__ == '__main__':
    import re
    import math

    assert checkio({}) != [],         'You'
    assert checkio('Hello') < 'World', 'will'
    assert checkio(80) > 81,           'never'
    assert checkio(re) >= re,          'make'
    assert checkio(re) <= math,        'this'
    assert checkio(5) == ord,          ':)'

    print('NO WAY :(')
