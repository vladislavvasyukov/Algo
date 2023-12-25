class ListNode:
    __slots__ = ("key", "prev_node", "next_node")
    def __init__(self, key, prev_node = None, next_node = None):
        self.key = key
        self.prev_node = prev_node
        self.next_node = next_node


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.current_size = 0
        self.cache = dict()
        self.head = None
        self.tail = None
        self.last_updated = None

    def _make_last_used(self, node):
        if self.last_updated == node:
            return

        key = node.key
        if node.prev_node:
            node.prev_node.next_node = node.next_node
        else:
            self.head = self.head.next_node
        if node.next_node:
            node.next_node.prev_node = node.prev_node
        else:
            self.tail = self.tail.prev_node

        new_node = ListNode(key=key, next_node=self.last_updated.next_node, prev_node=self.last_updated)
        self.last_updated.next_node = new_node
        if new_node.next_node is not None:
            new_node.next_node.prev_node = new_node
        if self.tail == self.last_updated:
            self.tail = new_node

        self.last_updated = new_node
        self.cache[key]["node"] = new_node


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self._make_last_used(self.cache[key]["node"])
        return self.cache[key]["value"]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key]["value"] = value
            self._make_last_used(self.cache[key]["node"])
            return

        if self.current_size == self.capacity:
            if self.last_updated == self.tail:
                self.cache.pop(self.head.key)
                self.head.key = key
                self.cache[key] = {
                    "value": value,
                    "node": self.head
                }
            else:
                self.cache.pop(self.last_updated.next_node.key)
                self.last_updated.next_node.key = key
                self.cache[key] = {
                    "value": value,
                    "node": self.last_updated.next_node
                }
            if self.last_updated == self.tail:
                self.last_updated = self.head
            else:
                self.last_updated = self.last_updated.next_node
        else:
            if self.head is None:
                new_node = ListNode(key=key)
                self.head = new_node
            else:
                new_node = ListNode(key=key, prev_node=self.tail)
                self.tail.next_node = new_node

            self.tail = new_node
            self.current_size += 1
            self.cache[key] = {
                "value": value,
                "node": self.tail
            }
            self.last_updated = self.tail



def test1():
    res = []
    obj = LRUCache(capacity=2)
    res.append(obj.put(1,1))
    res.append(obj.put(2, 2))
    res.append(obj.get(1))
    res.append(obj.put(3, 3))
    res.append(obj.get(2))
    res.append(obj.put(4, 4))
    res.append(obj.get(1))
    res.append(obj.get(3))
    res.append(obj.get(4))
    return res


def test2():
    res = []
    obj = LRUCache(capacity=2)
    res.append(obj.put(2,1))
    res.append(obj.put(2, 2))
    res.append(obj.get(2))
    res.append(obj.put(1, 1))
    res.append(obj.put(4, 1))
    res.append(obj.get(2))
    return res


def test3():
    res = []
    obj = LRUCache(capacity=2)
    res.append(obj.put(2,1))
    res.append(obj.put(1, 1))
    res.append(obj.put(2, 3))
    res.append(obj.put(4, 1))
    res.append(obj.get(1))
    res.append(obj.get(2))
    return res


def test4():
    res = []
    obj = LRUCache(capacity=3)
    res.append(obj.put(1,1))
    res.append(obj.put(2, 2))
    res.append(obj.put(3, 3))
    res.append(obj.put(4, 4))
    res.append(obj.get(4))
    res.append(obj.get(3))
    res.append(obj.get(2))
    res.append(obj.get(1))
    res.append(obj.put(5, 5))
    res.append(obj.get(1))
    res.append(obj.get(2))
    res.append(obj.get(3))
    res.append(obj.get(4))
    res.append(obj.get(5))
    return res


def test5():
    operations = ["put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
    args = [[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]

    res = []
    obj = LRUCache(capacity=10)
    for i in range(len(operations)):
        op = operations[i]
        op_args = args[i]
        tmp = getattr(obj, op)(*op_args)
        res.append(tmp)
        print(len(obj.cache))
    print(res)
    return res


if __name__ == "__main__":
    assert test1() == [None, None, 1, None, -1, None, -1, 3, 4]
    assert test2() == [None, None, 2, None, None, -1]
    assert test3() == [None, None, None, None, -1, 3]
    assert test4() == [None, None, None, None,4,3,2,-1, None,-1,2,3,-1,5]
    assert test5() == [None, None, None, None, None,-1, None,19,17, None,-1, None, None, None,-1, None,-1,5,-1,12, None, None,3,5,5, None, None,1, None,-1, None,30,5,30, None, None, None,-1, None,-1,24, None, None,18, None, None, None, None,-1, None, None,18, None, None,-1, None, None, None, None, None,18, None, None,-1, None,4,29,30, None,12,-1, None, None, None, None,29, None, None, None, None,17,22,18, None, None, None,-1, None, None, None,20, None, None, None,-1,18,18, None, None, None, None,20, None, None, None, None, None, None, None]
