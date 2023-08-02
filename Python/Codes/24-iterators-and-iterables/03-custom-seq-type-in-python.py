# Fibonacci Sequence :
class Fibonacci:
    def __init__(self, n):
        self.n = n

    def __getitem__(self, k):
        if isinstance(k, slice):
            start, stop, step = k.indices(self.n)
            return [self[i] for i in range(start, stop, step)]
        elif isinstance(k, int):
            if k < 0:
                k = self.n + k
            if k < 0 or k >= self.n:
                raise IndexError
            a, b = 0, 1
            for i in range(k):
                a, b = b, a + b
            return a
        else:
            raise TypeError

    def __len__(self):
        return self.n