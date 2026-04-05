class Solution:
    def decodeCiphertext(self, s: str, m: int) -> str:
        n = len(s)//m
        return ''.join(s[j::n+1] for j in range(n)).rstrip()