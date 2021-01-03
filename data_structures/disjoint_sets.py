class DisjointSets:
    # TODO написать методы для вычисления количества деревьев и из визуализации

    def __init__(self, size=0):
        self.parent = [None for _ in range(size)]
        self.rank = [None for _ in range(size)]

    def make_set(self, i):
        self.parent[i] = i
        self.rank[i] = 0

    def find(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])

        return self.parent[i]

    def union(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)

        if i_id == j_id:
            return

        if self.rank[i_id] > self.rank[j_id]:
            self.parent[j_id] = i_id
        else:
            self.parent[i_id] = j_id
            if self.rank[i_id] == self.rank[j_id]:
                self.rank[j_id] = self.rank[j_id] + 1

    def get_max_tree_high(self):
        max_high = 0
        for i in range(1, len(self.parent)):
            high = 0
            t = i
            while t != self.parent[t]:
                t = self.parent[t]
                high += 1

            if high > max_high:
                max_high = high

        return max_high


if __name__ == '__main__':
    ds = DisjointSets(13)

    for i in range(1, 13):
        ds.make_set(i)

    ds.union(2, 10)
    ds.union(7, 5)
    ds.union(6, 1)
    ds.union(3, 4)
    ds.union(5, 11)
    ds.union(7, 8)
    ds.union(7, 3)
    ds.union(12, 2)
    ds.union(9, 6)

    print('max = ', ds.get_max_tree_high())
