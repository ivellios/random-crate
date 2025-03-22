class RangeDict(dict):
    def __getitem__(self, key):
        # Check if key matches any range-like tuple
        for range_key in self:
            if isinstance(range_key, tuple) and len(range_key) == 2:
                low, high = range_key
                if low <= key <= high:
                    return super().__getitem__(range_key)
        raise KeyError(f"No matching range for key: {key}")

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default
