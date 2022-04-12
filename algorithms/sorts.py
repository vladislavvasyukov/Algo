def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i = i + 1
            else:
                array[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            array[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            array[k] = right_half[j]
            j = j + 1
            k = k + 1


def shell_sort(array):
    count = len(array)
    h = 1

    while h < count // 3:
        h = 3*h + 1

    while h >= 1:
        for i in range(h, count):
            j = i
            while j >= h and array[j-h] > array[j]:
                array[j-h], array[j] = array[j], array[j-h]
                print(array)
                j -= h
        h = h // 3


def quick_sort(array, left, right):
    if left < right:
        mid = partition(array, left, right)
        quick_sort(array, left, mid-1)
        quick_sort(array, mid+1, right)


def quick_sort_with_partition3(array, left, right):
    if left < right:
        m1, m2 = partition3(array, left, right)
        quick_sort(array, left, m1-1)
        quick_sort(array, m2+1, right)


def partition(array, left, right):
    el = array[right]
    i = left - 1
    for j in range(left, right):
        if array[j] < el:
            i += 1
            array[j], array[i] = array[i], array[j]

    i += 1
    array[i], array[right] = array[right], array[i]
    return i


def partition3(array, left, right):
    x = array[left]
    m1, m2 = left, right
    i = left

    while i <= m2:
        if array[i] < x:
            array[i], array[m1] = array[m1], array[i]
            m1 += 1

        elif array[i] > x:
            array[i], array[m2] = array[m2], array[i]
            i -= 1
            m2 -= 1

        i += 1

    return m1, m2


def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j-1]:
            array[j - 1], array[j] = array[j], array[j-1]
            j -= 1
