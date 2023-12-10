from typing import Iterable
from itertools import product


def flatten_tuple(t):
    # (1, (2, 3), (4, 5)) -> (1, 2, 3, 4, 5)
    for it in t:
        if isinstance(it, tuple) or isinstance(it, list):
            for element in it:
                yield element
        else:
            yield it


def tupledict(*coords: list[Iterable], rule):
    kvs = []
    assert len(coords) > 0
    for coord in product(*coords):
        # (1, (2, 3), (4, 5)) -> (1, 2, 3, 4, 5)
        coord = tuple(flatten_tuple(coord))
        value = rule(*coord)
        if len(coord) == 1:
            coord = coord[0]
        if value is not None:
            kvs.append((coord, value))
    return dict(kvs)
