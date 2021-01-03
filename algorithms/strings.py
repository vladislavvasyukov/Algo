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


if __name__ == '__main__':
    print(naive_search('aaabbb', 'b'))
    print(naive_search('aaabbb', 'bb'))
    print(naive_search('aaabbb', 'bbb'))
    print(naive_search('aaabbb', 'bbbb'))
