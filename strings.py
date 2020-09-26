def naive_search(text, pattern):
    text_length = len(text)
    pattern_length = len(pattern)
    result = []

    for i in range(text_length - pattern_length + 1):
        for j in range(pattern_length):
            if text[i+j] != pattern[j]:
                break
        else:
            result.append(i)
    return result


def compute_prefix_function(P):
    m = len(P)
    pi = [None for _ in range(m)]
    pi[0] = 0
    k = 0
    for q in range(1, m):
        while k > 0 and P[k+1] != P[q]:
            k = pi[k]
        if P[k+1] == P[q]:
            k += 1
        pi[q] = k
    return pi


def kmp_matcher(T, P):
    n = len(T)
    m = len(P)
    pi = compute_prefix_function(P)
    q = 0  # количество совпадающих символов
    for i in range(n):  # сканирование текста слева направо
        print(P, T, q+1, i)
        print()
        while q > 0 and P[q+1] != T[i]:
            q = pi[q]  # Следующий символ не совпадает
        if P[q+1] == T[i]:
            q += 1  # Следующий символ совпадает
        if q == m:  # Совпадает ли весь образец P
            print('FIND ', i-m)
            q = pi[q]  # Ищем следующее совпадение


if __name__ == '__main__':
    print(naive_search('aaabbb', 'b'))
    print(naive_search('aaabbb', 'bb'))
    print(naive_search('aaabbb', 'bbb'))
    print(naive_search('aaabbb', 'bbbb'))

    # kmp_matcher('aaabbb', 'b')
