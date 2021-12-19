class Unique:
    
    def __init__(self, data, **kwargs):
        self.used_elements = set()
        self.data = data
        self.i = 0
        self.ic = len(kwargs) > 0

    def __iter__(self):
        return self

    def __next__(self):
        while (self.i < len(self.data)):
            if isinstance(self.data[self.i], str) and self.ic:
                s = self.data[self.i].lower()
            else:
                s = self.data[self.i]
            if s not in self.used_elements:
                self.used_elements.add(s)
                return s    
            self.i += 1
        self.i = 0    
        raise StopIteration