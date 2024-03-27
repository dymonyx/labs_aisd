class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        unique_substrings = set()
        n = len(text)
        for length in range(1, n // 2 + 1):
            for i in range(n - length * 2 + 1):
                if text[i:i+length] == text[i+length:i+length*2]:
                    unique_substrings.add(text[i:i+length*2])
        return len(unique_substrings)