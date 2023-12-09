class AxisArray:
    def __init__(self, values, coords=None):
        self.values = values
        D = values.ndim
        if coords is None:
            self.dim_names = [None] * D
            self.name_to_dim = dict()
            self.dim_coord = [None] * D
        else:
            assert len(coords) == D
            self.dim_names = list(coords.keys())
            self.name_to_dim = {name: i for i, name in enumerate(self.dim_names)}
            self.dim_coord = list(coords.values())
        dim_lookup = [None] * D
        for dim, coord in enumerate(self.dim_coord):
            if coord is not None:
                dim_lookup[dim] = {v: i for i, v in enumerate(coord)}
        self.dim_lookup = dim_lookup

    def set_icoord(self, dim, coord):
        self.dim_coord[dim] = coord
        self.dim_lookup[dim] = {v: i for i, v in enumerate(coord)}

    def set_coord(self, name, coord):
        dim = self.name_to_dim.get(name, None)
        if dim is None:
            raise KeyError(f"Dimension {name} not found")
        self.dim_coord[dim] = coord
        self.dim_lookup[dim] = {v: i for i, v in enumerate(coord)}

    def get_icoord(self, dim):
        return self.dim_coord[dim]

    def get_coord(self, name):
        dim = self.name_to_dim.get(name, None)
        if dim is None:
            raise KeyError(f"Dimension {name} not found")
        return self.dim_coord[dim]

    def __getitem__(self, item):
        return self.values[item]

    def __setitem__(self, item, value):
        self.values[item] = value

    def v(self, *labels):
        indices = []
        for dim, index in enumerate(labels):
            lookup = self.dim_lookup[dim]
            if lookup is None:
                indices.append(index)
            else:
                indices.append(lookup[index])
        return self.values[tuple(indices)]

    def sv(self, labels: tuple, value):
        indices = []
        for dim, index in enumerate(labels):
            lookup = self.dim_lookup[dim]
            if lookup is None:
                indices.append(index)
            else:
                indices.append(lookup[index])
        self.values[tuple(indices)] = value

    def v_kw(self, **labels_kw):
        indices = [slice(None)] * self.values.ndim
        for name, index in labels_kw.items():
            dim = self.name_to_dim.get(name, None)
            if dim is None:
                raise KeyError(f"Dimension {name} not found")
            lookup = self.dim_lookup[dim]
            if lookup is None:
                indices[dim] = index
            else:
                indices[dim] = lookup[index]
        return self.values[tuple(indices)]

    def sv_kw(self, labels_dict, value):
        indices = [slice(None)] * self.values.ndim
        for name, index in labels_dict.items():
            dim = self.name_to_dim.get(name, None)
            if dim is None:
                raise KeyError(f"Dimension {name} not found")
            lookup = self.dim_lookup[dim]
            if lookup is None:
                indices[dim] = index
            else:
                indices[dim] = lookup[index]
        self.values[tuple(indices)] = value
