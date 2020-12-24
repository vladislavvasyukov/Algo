def binary_search(array, value):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == value:
            return mid

        elif array[mid] < value:
            left = mid + 1

        elif array[mid] > value:
            right = mid - 1

    return -1


if __name__ == '__main__':
    print(binary_search([-2, 0, 3, 3, 9, 23, 32, 89], -2))
