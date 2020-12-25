class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop()

    def __len__(self):
        return len(self.items)

    def size(self):
        return len(self)

    def empty(self):
        return self.size() == 0
