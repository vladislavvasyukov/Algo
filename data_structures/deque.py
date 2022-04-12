class Deque:
    def __init__(self):
        self.items = []

    def push_back(self, item):
        self.items.append(item)

    def push_front(self, item):
        self.items.insert(0, item)

    def pop_back(self):
        return self.items.pop()

    def pop_front(self):
        return self.items.pop(0)

    def __len__(self):
        return len(self.items)


def palindrome_checker(string):
    deque = Deque()
    for ch in string:
        deque.push_back(ch)

    checked = True
    while len(deque) > 1:
        front = deque.pop_front()
        back = deque.pop_back()
        if front != back:
            checked = False
            break
    return checked
