def can_be_segmented(s, words):
    words = set(words)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n+1):
        for j in range(i):
            if not dp[j]:
                continue
            if s[j:i] in words:
                dp[i] = True
                break
    return dp[n]



if __name__ == '__main__':
    print(can_be_segmented("leetcodeleet", ["leet", "code"]))