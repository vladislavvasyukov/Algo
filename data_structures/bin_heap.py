from math import inf


class BinHeap:
    FIRST_INDEX = 1

    def __init__(self):
        self.elems = [0]
        self.current_size = 0

    def sift_up(self, i):
        while i > 1 and self.elems[i // 2] < self.elems[i]:
            self.elems[i // 2], self.elems[i] = self.elems[i], self.elems[i // 2]
            i = i // 2

    def sift_down(self, i):
        while True:
            max_child_index = self.get_max_child_index(i)
            if i != max_child_index:
                self.elems[i], self.elems[max_child_index] = self.elems[max_child_index], self.elems[i]
                i = max_child_index
            else:
                break

    def get_max_child_index(self, i):
        """
        Возвращает индекс меньшего из двух потомков
        """

        max_child_index = i

        left_child_index = 2 * i
        if left_child_index <= self.current_size and self.elems[left_child_index] > self.elems[max_child_index]:
            max_child_index = left_child_index

        right_child_index = 2 * i + 1
        if right_child_index <= self.current_size and self.elems[right_child_index] > self.elems[max_child_index]:
            max_child_index = right_child_index

        return max_child_index

    def insert(self, k):
        """
        Добавляет новый элемент в кучу
        """
        self.elems.append(k)
        self.current_size += 1
        self.sift_up(self.current_size)

    def extract_max(self):
        """
        Удаляет и возвращает наименьший элемент кучи
        """
        max_value = self.elems[self.FIRST_INDEX]
        self.elems[self.FIRST_INDEX] = self.elems[self.current_size]
        self.elems.pop()
        self.current_size -= 1
        self.sift_down(self.FIRST_INDEX)
        return max_value

    def remove(self, i):
        self.elems[i] = inf
        self.sift_up(i)
        self.extract_max()

    def change_priority(self, i, p):
        old_priority = self.elems[i]
        self.elems[i] = p

        if p > old_priority:
            self.sift_up(i)
        else:
            self.sift_down(i)

    @classmethod
    def create(cls, array):
        heap = cls()
        for a in array:
            heap.insert(a)
        return heap

    @classmethod
    def create_heap_from_array(cls, array):
        heap = cls()
        heap.elems = array
        heap.current_size = len(array)
        array.insert(0, 0)

        for i in range(heap.current_size // 2, 0, -1):
            heap.sift_down(i)

        return heap

    @classmethod
    def heap_sort(cls, array):
        h = cls.create_heap_from_array(array)

        for i in range(h.current_size-1):
            h.elems[h.FIRST_INDEX], h.elems[h.current_size] = h.elems[h.current_size], h.elems[h.FIRST_INDEX],
            h.current_size -= 1
            h.sift_down(h.FIRST_INDEX)

        array.pop(0)

    @classmethod
    def partial_sort(cls, array, count_elements):
        heap = cls.create_heap_from_array(array)

        result = []
        for i in range(1, count_elements + 1):
            result.append(heap.extract_max())

        return result
