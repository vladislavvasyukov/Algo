from math import inf


class BinHeap:
    FIRST_ELEMENT_INDEX = 1

    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def sift_up(self, i):
        while i > 1 and self.heap_list[i // 2] < self.heap_list[i]:
            self.heap_list[i // 2], self.heap_list[i] = self.heap_list[i], self.heap_list[i // 2]
            i = i // 2

    def sift_down(self, i):
        while True:
            max_child_index = self.get_max_child_index(i)
            if i != max_child_index:
                self.heap_list[i], self.heap_list[max_child_index] = self.heap_list[max_child_index], self.heap_list[i]
                i = max_child_index
            else:
                break

    def get_max_child_index(self, i):
        """
        Возвращает индекс меньшего из двух потомков
        """

        max_child_index = i

        left_child_index = 2 * i
        if left_child_index <= self.current_size and self.heap_list[left_child_index] > self.heap_list[max_child_index]:
            max_child_index = left_child_index

        right_child_index = 2 * i + 1
        if right_child_index <= self.current_size and self.heap_list[right_child_index] > self.heap_list[max_child_index]:
            max_child_index = right_child_index

        return max_child_index

    def insert(self, k):
        """
        Добавляет новый элемент в кучу
        """
        self.heap_list.append(k)
        self.current_size += 1
        self.sift_up(self.current_size)

    def extract_max(self):
        """
        Удаляет и возвращает наименьший элемент кучи
        """
        max_value = self.heap_list[self.FIRST_ELEMENT_INDEX]
        self.heap_list[self.FIRST_ELEMENT_INDEX] = self.heap_list[self.current_size]
        self.heap_list.pop()
        self.current_size -= 1
        self.sift_down(self.FIRST_ELEMENT_INDEX)
        return max_value

    def remove(self, i):
        self.heap_list[i] = inf
        self.sift_up(i)
        self.extract_max()

    def change_priority(self, i, p):
        old_priority = self.heap_list[i]
        self.heap_list[i] = p

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
        heap.heap_list = array
        heap.current_size = len(array)
        array.insert(0, 0)

        for i in range(heap.current_size // 2, 0, -1):
            bin_heap.sift_down(i)

        return heap

    @classmethod
    def heap_sort(cls, array):
        heap = cls.create_heap_from_array(array)

        for i in range(heap.current_size-1):
            tmp = heap.heap_list[heap.FIRST_ELEMENT_INDEX]
            heap.heap_list[heap.FIRST_ELEMENT_INDEX] = heap.heap_list[heap.current_size]
            heap.heap_list[heap.current_size] = tmp

            heap.current_size -= 1
            heap.sift_down(heap.FIRST_ELEMENT_INDEX)

        array.pop(0)

    @classmethod
    def partial_sort(cls, array, count_elements):
        heap = cls.create_heap_from_array(array)

        result = []
        for i in range(1, count_elements + 1):
            result.append(heap.extract_max())

        return result


if __name__ == '__main__':
    bin_heap = BinHeap.create([33, 17, 27, 14, 18, 9, 5, 3, 11, 19, 21, 20, 22])

    print(bin_heap.heap_list)
    print(BinHeap.partial_sort([33, 17, 27, 14, 18, 9, 5, 3, 11, 19, 21, 20, 22], 3))

    arr = [33, 17, 27, 14, 18, 9, 5, 3, 11, 19, 21, 20, 22]
    BinHeap.heap_sort(arr)
    print(arr)

    # print(bin_heap.extract_max())
    # print(bin_heap.extract_max())
    # print(bin_heap.extract_max())
    # print(bin_heap.heap_list)

    # bin_heap = BinHeap.my_create([33, 17, 27, 14, 18, 9, 5, 11, 19, 21, 20])
    # print(bin_heap.heap_list)

