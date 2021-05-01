class FlexibleDict(dict):
    def __getitem__(self, key):
        try:
            return super().__getitem__(key)
        except KeyError:
            if isinstance(key, int):
                return super().__getitem__(str(key))
            return super().__getitem__(int(key))


