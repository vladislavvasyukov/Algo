from random import randint


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


def rabin_karp_matcher(text, pattern, d, q):
    n = len(text)
    m = len(pattern)
    h = pow(d, m-1) % q
    p = 0
    t = 0
    result = []
    for i in range(m):  # preprocessing
        p = (d*p+ord(pattern[i])) % q
        t = (d*t+ord(text[i])) % q
    for s in range(n-m+1):  # note the +1
        if p == t:  # check character by character
            match = True
            for i in range(m):
                if pattern[i] != text[s+i]:
                    match = False
                    break
            if match:
                result = result + [s]
        if s < n-m:
            t = (t-h*ord(text[s])) % q  # remove letter s
            t = (t*d+ord(text[s+m])) % q  # add letter s+m
            t = (t+q) % q  # make sure that t >= 0
    return result


if __name__ == '__main__':
    print(naive_search('aaabbb', 'b'))
    print(naive_search('aaabbb', 'bb'))
    print(naive_search('aaabbb', 'bbb'))
    print(naive_search('aaabbb', 'bbbb'))

    print()

    print(rabin_karp_matcher("3141592653589793", "26", 257, 11))
    print(rabin_karp_matcher("xxxxx", "xx", 40999999, 999999937))
