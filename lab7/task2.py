import re


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


with open('task2_article.txt', 'r', encoding='utf-8') as article:
    article_str_pre = article.read()
with open('task2_essay.txt', 'r', encoding='utf-8') as essay:
    essay_str = essay.read()

essay_arr = re.findall(r'\b\w+\b', essay_str.lower())
article_arr = re.findall(r'\b\w+\b', article_str_pre.lower())
article_str = ' '.join(article_arr)

patterns = []
for i in range(0, len(essay_arr) - 2, 3):
    patterns.append(' '.join([essay_arr[i], essay_arr[i + 1], essay_arr[i + 2]]))
prefixes = [prefix(pattern) for pattern in patterns]

plagiat = ''
for i in range(len(patterns)):
    if len(kmp(article_str, patterns[i], prefixes[i])) > 0:
        plagiat += patterns[i]

percent = len(plagiat) / len(article_str_pre) * 100
print(f'Процент плагиата: {percent}%')
