# yds

## Description

yds is a Python project that provides some small utilities of data structures.

## Usage

### Tupledict

The `tupledict` is a utility that allows you to create a dictionary with tuple keys. It provides a `select` method that can be used to retrieve values based on specific keys or a wildcard.

Here's an example of how to use `tupledict`:

```python
from yds.tupledict import tupledict, WILDCARD

# Create a tupledict instance
td = tupledict(
    {
        (1, 2): "a",
        (1, 3): "b",
        (2, 2): "c",
        (2, 3): "d",
    }
)

# Select with specific keys
print(list(td.select(1, 2)))  # Output: ["a"]

# Select with wildcard
print(list(td.select(WILDCARD, 2)))  # Output: ["a", "c"]
```

### AxisArray

The `AxisArray` is a utility that allows you to create a multidimensional array with labeled axes. It provides methods for indexing, slicing, and setting values in the array along any of its axes.

Here's an example of how to use `AxisArray`:

```python
from yds.axisarray import AxisArray

# Create an AxisArray instance
aa = AxisArray(
    values=[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    coords={'x': ['a', 'b', 'c'], 'y': ['d', 'e', 'f']}
)

# Indexing
print(aa.v('a', 'd'))  # Output: 1
print(aa.v_kw(x='a', y='d'))  # Output: 1

# Setting values
aa.sv(('a', 'd'), 10)
print(aa.v('a', 'd'))  # Output: 10

aa.sv_kw(dict(x='a', y='d'), 20)
print(aa.v(x='a', y='d'))  # Output: 20
```

## Contributing

If you want to contribute to this project, please follow these steps:

1. Fork the repository
2. Create a new branch: `git checkout -b feature_branch_name`
3. Make your changes
4. Push to your branch: `git push origin feature_branch_name`
5. Create a Pull Request

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.