import random


def prime(x):
    return all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))


def prefix(s):
    m = len(s)
    pi = [0] * m
    k = 0
    for q in range(1, m):
        while k > 0 and s[k] != s[q]:
            k = pi[k - 1]
        if s[k] == s[q]:
            k += 1
        pi[q] = k
    return pi


def kmp(s, pattern, prefixes):
    pattern_len = len(pattern)
    text_len = len(s)
    matches = []
    i = j = 0
    while i < text_len and j < pattern_len:
        if s[i] == pattern[j]:
            if j == pattern_len - 1:
                matches.append(i - pattern_len + 1)
                j = 0
            else:
                j += 1
            i += 1
        elif j:
            j = prefixes[j - 1]
        else:
            i += 1
    return matches


if __name__ == '__main__':

    s = ''

    for i in range(500):
        x = random.randint(2, 1000)
        if prime(x):
            s += str(x)
    print(s)

    patterns = [str(i) for i in range(10, 100)]
    prefixes = [prefix(i) for i in patterns]

    arr = []
    for i in range(len(patterns)):
        arr.append(len(kmp(s, patterns[i], prefixes[i])))

    num = patterns[arr.index(max(arr))]

    print(num, max(arr))
