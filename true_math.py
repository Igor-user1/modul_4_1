from math import inf


def divide(first, second):
    if second != 0:
        return first/second
    else:
        if first >= 0:
            return inf
        else:
            return -inf
