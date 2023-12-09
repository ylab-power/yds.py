from yds.tupledict import flatten_tuple, tupledict


def test_flatten_tuple():
    assert list(flatten_tuple((1, (2, 3), (4, 5)))) == [1, 2, 3, 4, 5]
    assert list(flatten_tuple((1, 2, 3))) == [1, 2, 3]
    assert list(flatten_tuple(((1, 2), 3))) == [1, 2, 3]


def test_tupledict():
    assert tupledict([1, 2], [3, 4], rule=lambda x, y: x * y) == {
        (1, 3): 3,
        (1, 4): 4,
        (2, 3): 6,
        (2, 4): 8,
    }
    assert tupledict([1, 2], [3, 4], rule=lambda x, y: None) == {}
    assert tupledict([1, 2], rule=lambda x: x) == {1: 1, 2: 2}
    assert tupledict([1, 2], [(3, 3), (4, 4)], rule=lambda x, y, z: x) == {
        (1, 3, 3): 1,
        (1, 4, 4): 1,
        (2, 3, 3): 2,
        (2, 4, 4): 2,
    }
