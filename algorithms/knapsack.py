from collections import namedtuple


def knapsack_without_repetitions(total_weight: int, elements):
    matrix = []
    for i in range(total_weight+1):
        row = [None for _ in range(len(elements)+1)]
        matrix.append(row)

    for i in range(total_weight+1):
        matrix[i][0] = 0

    for j in range(len(elements)+1):
        matrix[0][j] = 0

    for i in range(1, len(elements) + 1):
        element = elements[i-1]
        for weight in range(1, total_weight+1):
            matrix[weight][i] = matrix[weight][i-1]
            if element.weight <= weight:
                value = matrix[weight-element.weight][i-1] + element.value
                if value > matrix[weight][i]:
                    matrix[weight][i] = value

    print('=========================')
    for row in matrix:
        print(' '.join([str(r) + '\t' for r in row]))
    print('=========================')

    return matrix[total_weight][len(elements)]


def knapsack_with_repetitions(total_weight: int, elements):
    result = [0] * (total_weight+1)
    for weight in range(1, total_weight+1):
        for element in elements:
            if weight >= element.weight:
                value = result[weight-element.weight] + element.value
                if value > result[weight]:
                    result[weight] = value

    return result[total_weight]


if __name__ == '__main__':
    Element = namedtuple('Element', ['weight', 'value'])
    elements = [
        Element(value=30, weight=6),
        Element(value=14, weight=3),
        Element(value=16, weight=4),
        Element(value=9, weight=2),
    ]
    print(knapsack_without_repetitions(10, elements))
    print(knapsack_with_repetitions(10, elements))
