class FlexibleDict(dict):
    def __getitem__(self, key):
        try:
            return super().__getitem__(key)
        except KeyError:
            if isinstance(key, int):
                return super().__getitem__(str(key))
            return super().__getitem__(int(key))


class StringKeyDict(dict):
    def __setitem__(self, k, v):
        super().__setitem__(str(k), v)


class RecentDict(dict):
    def __init__(self, n_max):
        super().__init__()
        self.n_max = n_max
    
    def __len__(self) -> int:
        return super().__len__()
    
    def __setitem__(self, k, v):
        if self.__len__() == self.n_max:
            oldest_key = list(self.keys())[0]
            del self[oldest_key]
        super().__setitem__(k, v)


# d = RecentDict(3)
# d['a'] = 2
# print(d)
# d['b'] = 3
# print(d)
# d['c'] = 4
# print(d)
# d['d'] = 5
# print(d)


class FlatList(list):
    def append(self, __object) -> None:
        try:
            iterator = iter(__object)
            for x in iterator:
                super().append(x)
        except TypeError:
            super().append(__object)

f = FlatList()
f.append(4)
print(f)
f.append(6)
print(f)
f.append(10)
print(f)
f.append([1,2,3])
print(f)