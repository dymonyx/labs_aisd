import random

s = ''


def prime(x):
    return all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))


for i in range(500):
    x = random.randint(2, 1000)
    if prime(x):
        s += str(x)
print(s)


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


patterns = [str(i) for i in range(10, 100)]
prefixes = [prefix(i) for i in patterns]
print(prefixes)


def kmp(s, pattern, prefixes):
    n = len(s)
    m = len(pattern)
    q = 0
    matches = []
    for i in range(n):
        while q > 0 and pattern[q] != s[i]:
            q = prefixes[q - 1]
        if pattern[q] == s[i]:
            q += 1
        if q == m:
            matches.append(i - m + 1)
            q = prefixes[q - 1]
    return matches


arr = []
for i in range(len(patterns)):
    arr.append(len(kmp(s, patterns[i], prefixes[i])))

num = patterns[arr.index(max(arr))]

print(num, max(arr))
