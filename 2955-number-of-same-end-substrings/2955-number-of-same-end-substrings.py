class Solution:
    def sameEndSubstringCount(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s) + 1
        char_sums = {c: [0] * n for c in ascii_lowercase}
        for i, ch in enumerate(s, 1):
            for c in ascii_lowercase:
                if c == ch:
                    char_sums[c][i] = char_sums[c][i - 1] + 1
                else:
                    char_sums[c][i] = char_sums[c][i - 1]
                    
        ans = []
        for l, r in queries:
            count = 0
            for c in ascii_lowercase:
                t = char_sums[c][r + 1] - char_sums[c][l]
                count += t * (t + 1) // 2
            ans.append(count)
        return ans