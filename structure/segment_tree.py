class SegmentTree:
    def __init__(self, size):
        self.size = 1 << (size - 1).bit_length()
        self.tree = [0] * (self.size << 1)

    def __getitem__(self, i):
        return self.tree[i + self.size]

    def update(self, i, x):
        i += self.size
        while i > 0:
            self.tree[i] = x
            x = self.tree[i] + self.tree[i ^ 1]
            i >>= 1

    def range_sum(self, i, j):
        x = 0
        i += self.size
        j += self.size
        while i < j:
            if i & 1:
                x += self.tree[i]
                i += 1
            if j & 1:
                x += self.tree[j - 1]
            i >>= 1
            j >>= 1
        return x
