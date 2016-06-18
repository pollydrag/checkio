# Solution for "Letter Queue"
# https://checkio.org/mission/letter-queue/

import functools

def letter_queue(commands):
    return functools.reduce(
        lambda r, x: r[1:] if x == 'POP' else r + x[-1:],
        commands,
        ""
    )

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]) == "DOT", "dot example"
    assert letter_queue(["POP", "POP"]) == "", "Pop, Pop, empty"
    assert letter_queue(["PUSH H", "PUSH I"]) == "HI", "Hi!"
    assert letter_queue([]) == "", "Nothing"
