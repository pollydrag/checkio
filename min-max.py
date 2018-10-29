def lt(a, b, key=None):
    return key(a) < key(b) if key else a < b


def gt(a, b, key=None):
    return key(a) > key(b) if key else a > b


def min_max(*args, **kwargs):
    cmp = kwargs.get('cmp')
    key = kwargs.get('key')

    iterable = args[0] if len(args) == 1 else args

    ret = None
    for i in iterable:
        if ret is None or cmp(i, ret, key):
            ret = i

    return ret


def min(*args, **kwargs):
    return min_max(*args, cmp=lt, key=kwargs.get("key"))


def max(*args, **kwargs):
    return min_max(*args, cmp=gt, key=kwargs.get("key"))


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
