import pytest
import numpy as np
from yds.axisarray import AxisArray

@pytest.fixture
def axis_array():
    return AxisArray(np.array([[1, 2], [3, 4]]), {'x': [0, 1], 'y': [0, 1]})

def test_axisarray_init(axis_array):
    assert np.array_equal(axis_array.values, np.array([[1, 2], [3, 4]]))
    assert axis_array.dim_names == ['x', 'y']
    assert axis_array.name_to_dim == {'x': 0, 'y': 1}
    assert axis_array.dim_coord == [[0, 1], [0, 1]]
    assert axis_array.dim_lookup == [{0: 0, 1: 1}, {0: 0, 1: 1}]

def test_set_icoord(axis_array):
    axis_array.set_icoord(0, [0, 1])
    assert axis_array.dim_coord[0] == [0, 1]
    assert axis_array.dim_lookup[0] == {0: 0, 1: 1}

def test_set_coord(axis_array):
    axis_array.set_coord('x', [2, 3])
    assert axis_array.dim_coord[0] == [2, 3]
    assert axis_array.dim_lookup[0] == {2: 0, 3: 1}

def test_get_icoord(axis_array):
    assert axis_array.get_icoord(0) == [0, 1]

def test_set_coord_not_found(axis_array):
    with pytest.raises(KeyError):
        axis_array.set_coord('z', [2, 3])

def test_v(axis_array):
    assert axis_array.v(0, 1) == 2

def test_v_kw(axis_array):
    assert axis_array.v_kw(x=0, y=1) == 2

def test_sv(axis_array):
    axis_array.sv((0, 1), 5)
    assert axis_array.v(0, 1) == 5

def test_sv_kw(axis_array):
    axis_array.sv_kw(dict(x=0, y=1), value=5)
    assert axis_array.v_kw(x=0, y=1) == 5