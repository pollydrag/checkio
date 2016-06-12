import operator

def count_gold(pyramid):
    """
    Return max possible sum in a path from top to bottom

    Use dynamic loops like:
    def paths():
        for i0 in [0]:
            for i1 in [i0, i0 + 1]:
                for i2 in [i1, i1 + 1]:
                    yield i0, i1, i2
    """

    l = len(pyramid)

    code_ = ['def paths():']
    code_.extend(['for i{row} in [{scope}]:'.format(
        row=row,
        scope=0 if not row else ('i{prev_row}, i{prev_row} + 1'.format(prev_row=row - 1))
    ) for row in range(l)])
    code_.extend(['yield {vars}'.format(
        vars=','.join(['i%s' % i for i in range(l)])
    )])

    tab = ' ' * 4
    code_ = '\n'.join(map(lambda x: tab * x[0] + x[1], enumerate(code_)))
    exec(code_, globals())

    m = max(paths(), key=lambda x: sum(map(operator.getitem, pyramid, x)))
    return sum(map(operator.getitem, pyramid, m))


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_gold((
        (1,),
        (2, 3),
        (3, 3, 1),
        (3, 1, 5, 4),
        (3, 1, 3, 1, 3),
        (2, 2, 2, 2, 2, 2),
        (5, 6, 4, 5, 6, 4, 3)
    )) == 23, "First example"
    assert count_gold((
        (1,),
        (2, 1),
        (1, 2, 1),
        (1, 2, 1, 1),
        (1, 2, 1, 1, 1),
        (1, 2, 1, 1, 1, 1),
        (1, 2, 1, 1, 1, 1, 9)
    )) == 15, "Second example"
    assert count_gold((
        (9,),
        (2, 2),
        (3, 3, 3),
        (4, 4, 4, 4)
    )) == 18, "Third example"
