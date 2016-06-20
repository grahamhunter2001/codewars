from itertools import groupby
def unique_in_order(iterable):
    return [i for i, v in groupby(iterable)]
