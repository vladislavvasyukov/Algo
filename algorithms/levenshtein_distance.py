def edit_distance(first, second):
    len_first = len(first)
    len_second = len(second)

    matrix = [[0] + [a for a in range(1, len_second + 1)]]

    for j in range(1, len_first + 1):
        row = [j] + [0 for _ in range(len_second)]
        matrix.append(row)

    for j in range(1, len_second + 1):
        for i in range(1, len_first + 1):
            insertion = matrix[i][j - 1] + 1
            deletion = matrix[i - 1][j] + 1
            match = matrix[i - 1][j - 1]
            mismatch = matrix[i - 1][j - 1] + 1

            if first[i - 1] == second[j - 1]:
                matrix[i][j] = min([insertion, deletion, match])
            else:
                matrix[i][j] = min([insertion, deletion, mismatch])

    return matrix[len_first][len_second]


def print_matrix(matrix, first, second):
    print("*"*(len(second)+1))
    print(" \t" + " ".join([' \t'] + [a + '\t' for a in second]))
    for i, row in enumerate(matrix):
        tmp = ' \t' if i == 0 else f'{first[i-1]}\t'
        print(' '.join([tmp] + [str(a) + '\t' for a in row]))
    print("*"*(len(second)+1))
