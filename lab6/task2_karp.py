import re
def rabin_karp(pattern, text):
    global plagiat
    d = 256
    pattern_length = len(pattern)
    text_length = len(text)
    pattern_hash = 0
    text_hash = 0
    h = 1
    q = 101

    for i in range(pattern_length - 1):
        h = (h * d) % q

    for i in range(pattern_length):
        pattern_hash = (d * pattern_hash + ord(pattern[i])) % q
        text_hash = (d * text_hash + ord(text[i])) % q

    for i in range(text_length - pattern_length + 1):
        if pattern_hash == text_hash:
            j = 0
            while j < pattern_length:
                if text[i + j] != pattern[j]:
                    break
                j += 1

            if j == pattern_length:
                plagiat += pattern

        if i < text_length - pattern_length:
            text_hash = (d * (text_hash - ord(text[i]) * h) + ord(text[i + pattern_length])) % q

            if text_hash < 0:
                text_hash = (text_hash + q)


if __name__ == '__main__':
    plagiat = ''

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

    for i in range(len(patterns)):
        rabin_karp(patterns[i], article_str)

    percent = len(plagiat) / len(article_str_pre) * 100
    print(f'Процент плагиата: {percent}%')