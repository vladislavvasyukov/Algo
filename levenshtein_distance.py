def edit_distance(first, second):
    len_first = len(first)
    len_second = len(second)

    matrix = [[0] + [a for a in range(1, len_second + 1)]]

    for j in range(1, len_first + 1):
        row = [j, 0] + [0 for a in range(1, len_first + 1)]
        matrix.append(row)

    for j in range(1, len_second + 1):
        for i in range(1, len_first + 1):
            insertion = matrix[i][j - 1] + 1
            deletion = matrix[i - 1][j] + 1
            match = matrix[i - 1][j - 1]
            mismatch = matrix[i - 1][j - 1] + 1

            if first[i - 1] == second[j - 1]:  # attention for indexes
                matrix[i][j] = min([insertion, deletion, match])
            else:
                matrix[i][j] = min([insertion, deletion, mismatch])

    return matrix[len_first][len_second]


if __name__ == '__main__':
    first_word = input()
    second_word = input()
    print(edit_distance(first_word, second_word))
