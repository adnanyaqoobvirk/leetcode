class Solution:
    def sameEndSubstringCount(self, s: str, queries: List[List[int]]) -> List[int]:
        char_sums = {c: [0] for c in ascii_lowercase}
        for ch in s:
            for c in ascii_lowercase:
                char_sums[c].append(char_sums[c][-1])
                if c == ch:
                    char_sums[c][-1] += 1
                    
        ans = []
        for l, r in queries:
            count = 0
            for c in ascii_lowercase:
                t = char_sums[c][r + 1] - char_sums[c][l]
                count += t * (t + 1) // 2
            ans.append(count)
        return ans