class BinHeap:
    FIRST_ELEMENT_INDEX = 1

    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def increase_key(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                # Меняем родителя и предка местами
                self.heap_list[i // 2], self.heap_list[i] = self.heap_list[i], self.heap_list[i // 2]
            i = i // 2

    def insert(self, k):
        """
        Добавляет новый элемент в кучу
        """
        self.heap_list.append(k)
        self.current_size += 1
        self.increase_key(self.current_size)

    def decrease_key(self, i):
        while i * 2 <= self.current_size:
            mc = self.get_min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
            i = mc

    def get_min_child(self, i):
        """
        Возвращает индекс меньшего из двух потомков
        """
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i*2] < self.heap_list[i*2+1]:
                return i*2
            else:
                return i * 2 + 1

    def del_min(self):
        """
        Удаляет и возвращает наименьший элемент кучи
        """
        min_value = self.heap_list[self.FIRST_ELEMENT_INDEX]
        self.heap_list[self.FIRST_ELEMENT_INDEX] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self.decrease_key(self.FIRST_ELEMENT_INDEX)
        return min_value

    @classmethod
    def create(cls, array):
        heap = cls()
        for a in array:
            heap.insert(a)
        return heap


if __name__ == '__main__':
    bin_heap = BinHeap.create([33, 17, 27, 14, 18, 9, 5, 3, 11, 19, 21, 20, 22])
    print(bin_heap.heap_list)
    print(bin_heap.del_min())
    print(bin_heap.del_min())
    print(bin_heap.del_min())
    print(bin_heap.heap_list)

    # bin_heap = BinHeap.my_create([33, 17, 27, 14, 18, 9, 5, 11, 19, 21, 20])
    # print(bin_heap.heap_list)

